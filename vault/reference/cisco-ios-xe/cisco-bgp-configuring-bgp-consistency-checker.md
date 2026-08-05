---
title: "Configuring BGP Consistency Checker"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-configuring-bgp-consistency-checker
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 52 Configuring BGP Consistency Checker The BGP Consistency Checker feature provides a way to identify certain types of BGP route inconsistencies with peers: next-hop label inconsistency, RIB-out inconsistency, and aggregation inconsistency. Upon finding such an inconsistency, the system sends a syslog error message and takes appropriate action if configured to do so. • Finding Feature In"
---

# Configuring BGP Consistency Checker

CHAPTER

52

Configuring BGP Consistency Checker
The BGP Consistency Checker feature provides a way to identify certain types of BGP route inconsistencies
with peers: next-hop label inconsistency, RIB-out inconsistency, and aggregation inconsistency. Upon finding
such an inconsistency, the system sends a syslog error message and takes appropriate action if configured to
do so.
• Finding Feature Information, on page 839
• Information About BGP Consistency Checker, on page 839
• How to Configure BGP Consistency Checker, on page 840
• Configuration Examples for BGP Consistency Checker, on page 841
• Additional References, on page 841
• Feature Information for BGP Consistency Checker, on page 843

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Consistency Checker
BGP Consistency Checker
A BGP route inconsistency with a peer occurs when an update or a withdraw is not sent to a peer, and black-hole
routing can result. To identify that issue, BGP consistency checker was created as a low-priority process that
does nexthop-label, RIB-out, and aggregation consistency checks at a configurable interval. When enabled,
BGP consistency checker is performed for all address families. Configuring BGP consistency checker is
recommended.
Once the process identifies such an inconsistency, it will report the inconsistency with a syslog message and
optionally take action if the auto-repair keyword is specified. The action taken depends on the type of
inconsistency found.

IP Routing: BGP Configuration Guide
839


Configuring BGP Consistency Checker
How to Configure BGP Consistency Checker

• Next-Hop Label Consistency Check—When two paths have the same next hop because they are advertised
by the same provider edge router (PE), they should also have the same next-hop label. If the labels are
different, there is an inconsistency. If the auto-repair keyword is specified, the system will send a
route-refresh request.
• RIB-Out Consistency Check—If a network passes an outbound policy and is not sent, or if a network
does not pass an outbound policy and is sent, there is an inconsistency. If the auto-repair keyword is
specified, the system will send a route-refresh request.
• Aggregation Consistency Check—If specific routes and the aggregated route become out of sync, an
inconsistency can occur. Either the error-message keyword or the auto-repair keyword will trigger
aggregation reevaluation.
In the unlikely event that you receive a syslog message about an inconsistency, notify your Cisco technical
support representative with the syslog message exactly as it appears. The following are examples of such
syslog messages:
• “Net 10.0.0.0/32 has Nexthop-Label inconsistency.”
• “Net 10.0.0.0/32 in IPv4 Unicast has rib-out inconsistency for update-group 4 - outbound-policy fails.”

How to Configure BGP Consistency Checker
Configure BGP Consistency Checker
SUMMARY STEPS
1.
2.
3.
4.
5.
6.

enable
configure terminal
router bgp autonomous-system-number
bgp consistency-checker {error-message | auto-repair} [interval minutes]
end
show ip bgp [vpnv4 | vpnv6] all inconsistency nexthop-label

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
Example:
Router# configure terminal

IP Routing: BGP Configuration Guide
840

Enters global configuration mode.


Configuring BGP Consistency Checker
Configuration Examples for BGP Consistency Checker

Step 3

Command or Action

Purpose

router bgp autonomous-system-number

Configures a BGP routing process.

Example:
Router(config)# router bgp 500

Step 4

bgp consistency-checker {error-message | auto-repair} Enables BGP consistency checker.
[interval minutes]
• The default interval is 1440 minutes (one day). The
range is 5 to 1440 minutes.
Example:
Router(config-router)# bgp consistency-checker
auto-repair interval 720

Step 5

Ends the current configuration and returns to privileged
EXEC mode.

end
Example:
Router(config-router)# end

Step 6

show ip bgp [vpnv4 | vpnv6] all inconsistency
nexthop-label
Example:
Router# show ip bgp all inconsistency nexthop-label

(Optional) Displays routes that have a nexthop-label
inconsistency found.
• This step is not part of configuring the feature; it is
provided in case you receive a syslog message about
a nexthop-label inconsistency and you want to display
those routes.

Configuration Examples for BGP Consistency Checker
Example: Configuring BGP Consistency Checker
The following example configures BGP consistency checker with auto-repair at the default interval of one
day:
router bgp 65000
bgp consistency-checker auto-repair

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

IP Routing: BGP Configuration Guide
841


Configuring BGP Consistency Checker
Additional References

Related Topic

Document Title

Enabling BGP MIB support “BGP MIB Support” module in the IP Routing: BGP Configuration Guide
Configuring SNMP Support SNMP Configuration Guide in the Cisco IOS Network Management
Configuration Guide Library
SNMP Commands

Cisco IOS SNMP Support Command Reference

Standards
Standard Title
None

—

MIBs
MIB MIBs Link
—

To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFC

Title

RFC 1657 BGP-4 MIB
RFC 1771 A Border Gateway Protocol 4 (BGP-4)
RFC 2547 BGP/MPLS VPNs
RFC 2858 Multiprotocol Extensions for BGP-4
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

IP Routing: BGP Configuration Guide
842


Configuring BGP Consistency Checker
Feature Information for BGP Consistency Checker

Feature Information for BGP Consistency Checker
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 68: Feature Information for BGP Consistency Checker

Feature Name

Releases

Feature Information

BGP Consistency Cisco IOS XE Release The BGP Consistency Checker feature provides a way to
Checker
3.3S
identify three types of BGP route inconsistencies with peers:
next-hop label inconsistency, RIB-out inconsistency, and
Cisco IOS XE Release
aggregation inconsistency. Upon finding such inconsistency,
3.4SG
the system sends a syslog error message and takes appropriate
action if configured to do so.
The following command was introduced: bgp
consistency-checker
The following command was modified: show ip bgp vpnv4.

IP Routing: BGP Configuration Guide
843


Configuring BGP Consistency Checker
Feature Information for BGP Consistency Checker

IP Routing: BGP Configuration Guide
844
