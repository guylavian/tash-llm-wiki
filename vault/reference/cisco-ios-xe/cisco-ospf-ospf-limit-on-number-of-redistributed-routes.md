---
title: "OSPF Limit on Number of Redistributed Routes"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-limit-on-number-of-redistributed-routes
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 27 OSPF Limit on Number of Redistributed Routes Open Shortest Path First (OSPF) supports a user-defined maximum number of prefixes (routes) that are allowed to be redistributed into OSPF from other protocols or other OSPF processes. Such a limit could help prevent the router from being flooded by too many redistributed routes. • Finding Feature Information, page 263 • Prerequisites for O"
---

# OSPF Limit on Number of Redistributed Routes

CHAPTER

27

OSPF Limit on Number of Redistributed Routes
Open Shortest Path First (OSPF) supports a user-defined maximum number of prefixes (routes) that are
allowed to be redistributed into OSPF from other protocols or other OSPF processes. Such a limit could help
prevent the router from being flooded by too many redistributed routes.
• Finding Feature Information, page 263
• Prerequisites for OSPF Limit on Number of Redistributed Routes, page 263
• Information About OSPF Limit on Number of Redistributed Routes, page 264
• How to Limit the Number of OSPF Redistributed Routes, page 264
• Configuration Examples for OSPF Limit on Number of Redistributed Routes, page 267
• Additional References, page 268
• Feature Information for OSPF Limit on Number of Redistributed Routes, page 269

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPF Limit on Number of Redistributed Routes
It is presumed that you have OSPF configured in your network, along with another protocol or another OSPF
process you are redistributing.

IP Routing: OSPF Configuration Guide
263


OSPF Limit on Number of Redistributed Routes
Information About OSPF Limit on Number of Redistributed Routes

Information About OSPF Limit on Number of Redistributed Routes
If large number of IP routes are sent into OSPF by redistributing Border Gateway Protocol (BGP) into OSPF,
the network can be severely flooded. Limiting the number of redistributed routes prevents this potential
problem.
OSPF can receive and accept packets from non-routable addresses (for example, 0.0.0.0/7) also.

How to Limit the Number of OSPF Redistributed Routes
This section contains the following procedures, which are mutually exclusive. That is, you cannot both limit
redistributed prefixes and also choose to be warned.

Limiting the Number of Redistributed Routes
Note

You cannot both limit redistributed prefixes and also choose to be warned.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. redistribute protocol [process-id | as-number] [metric metric-value] [metric-type type-value]
[match{internal| external 1| external 2}][tag tag-value] [route-map map-tag] [subnets]
5. redistribute maximum-prefix maximum [threshold]
6. end
7. show ip ospf [process-id]

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

IP Routing: OSPF Configuration Guide
264

Enters global configuration mode.


OSPF Limit on Number of Redistributed Routes
Requesting a Warning About the Number of Routes Redistributed into OSPF

Step 3

Command or Action

Purpose

router ospf process-id

Configures an OSPF routing process.

Example:
Router(config)# router ospf 1

Step 4

redistribute protocol [process-id | as-number]
[metric metric-value] [metric-type type-value]
[match{internal| external 1| external 2}][tag
tag-value] [route-map map-tag] [subnets]

Redistributes routes from one routing domain into another
routing domain.

Example:
Router(config-router)# redistribute eigrp 10

Step 5

redistribute maximum-prefix maximum [threshold] Sets a maximum number of IP prefixes that are allowed to be
redistributed into OSPF.
Example:
Router(config-router)# redistribute
maximum-prefix 100 80

• There is no default value for the maximum argument.
• The threshold value defaults to 75 percent.
Note

Step 6

If the warning-only keyword had been configured in
this command, no limit would be enforced; a warning
message is simply logged.

Exits router configuration mode.

end
Example:
Router(config-router)# end

Step 7

show ip ospf [process-id]
Example:
Router# show ip ospf 1

(Optional) Displays general information about OSPF routing
processes.
• If a redistribution limit was configured, the output will
include the maximum limit of redistributed prefixes and
the threshold for warning messages.

Requesting a Warning About the Number of Routes Redistributed into OSPF
Note

You cannot both limit redistributed prefixes and also choose to be warned.

IP Routing: OSPF Configuration Guide
265


OSPF Limit on Number of Redistributed Routes
Requesting a Warning About the Number of Routes Redistributed into OSPF

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. redistribute protocol [process-id | as-number] [metric metric-value] [metric-type type-value]
[match{internal| external 1| external 2}][tag tag-value] [route-map map-tag] [subnets]
5. redistribute maximum-prefix maximum [threshold] warning-only
6. end

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

router ospf process-id

Configures an OSPF routing process.

Example:
Router(config)# router ospf 1

Step 4

redistribute protocol [process-id | as-number] [metric Redistributes routes from one routing domain into another
routing domain.
metric-value] [metric-type type-value]
[match{internal| external 1| external 2}][tag
tag-value] [route-map map-tag] [subnets]
Example:
Router(config-router)# redistribute eigrp 10

Step 5

redistribute maximum-prefix maximum [threshold] Causes a warning message to be logged when the maximum
number of IP prefixes has been redistributed into OSPF.
warning-only
Example:
Router(config-router)# redistribute
maximum-prefix 1000 80 warning-only

• Because the warning-only keyword is included, no limit
is imposed on the number of redistributed prefixes into
OSPF.
• There is no default value for the maximum argument.
• The threshold value defaults to 75 percent.

IP Routing: OSPF Configuration Guide
266


OSPF Limit on Number of Redistributed Routes
Configuration Examples for OSPF Limit on Number of Redistributed Routes

Command or Action

Purpose
• This example causes two warnings: one at 80 percent of
1000 (800 routes redistributed) and another at 1000 routes
redistributed.

Step 6

Exits router configuration mode.

end
Example:
Router(config-router)# end

Configuration Examples for OSPF Limit on Number of
Redistributed Routes
Example OSPF Limit the Number of Redistributed Routes
This example sets a maximum of 1200 prefixes that can be redistributed into OSPF process 1. Prior to reaching
the limit, when the number of prefixes redistributed reaches 80 percent of 1200 (960 prefixes), a warning
message is logged. Another warning is logged when the limit is reached and no more routes are redistributed.
router ospf 1
router-id 10.0.0.1
domain-id 5.6.7.8
log-adjacency-changes
timers lsa-interval 2
network 10.0.0.1 0.0.0.0 area 0
network 10.1.5.1 0.0.0.0 area 0
network 10.2.2.1 0.0.0.0 area 0
redistribute static subnets
redistribute maximum-prefix 1200 80

Example Requesting a Warning About the Number of Redistributed Routes
This example allows two warning messages to be logged, the first if the number of prefixes redistributed
reaches 85 percent of 600 (510 prefixes), and the second if the number of redistributed routes reaches 600.
However, the number of redistributed routes is not limited.
router ospf 1
network 10.0.0.0 0.0.0.255 area 0
redistribute eigrp 10 subnets
redistribute maximum-prefix 600 85 warning-only

IP Routing: OSPF Configuration Guide
267


OSPF Limit on Number of Redistributed Routes
Additional References

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

OSPFv3 Address Families

OSPFv3 Address Families module

Standards
Standards

Title

No new or modified standards are supported by this —
feature, and support for existing standards has not
been modified by this feature.

MIBs
MIBs

MIBs Link

No new or modified MIBs are supported by this
feature, and support for existing MIBs has not been
modified by this feature.

To locate and download MIBs for selected platforms,
Cisco software releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFCs

Title

RFC 5187.

OSPFv3 Graceful Restart

IP Routing: OSPF Configuration Guide
268


OSPF Limit on Number of Redistributed Routes
Feature Information for OSPF Limit on Number of Redistributed Routes

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

Feature Information for OSPF Limit on Number of Redistributed
Routes
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 30: Feature Information for OSPF Limit on Number of Redistributed Routes

Feature Name

Releases

Feature Information

OSPF Limit on Number of
Redistributed Routes

Cisco IOS XE Release 2.1 Cisco
IOS XE Release 2.6

OSPF supports a user-defined
maximum number of prefixes
(routes) that are allowed to be
redistributed into OSPF from other
protocols or other OSPF processes.
Such a limit could help prevent the
router from being flooded by too
many redistributed routes.
The following commands are
introduced or modified in the
feature documented in this module:
• redistribute
maximum-prefix
• show ip ospf
• show ip ospf database

IP Routing: OSPF Configuration Guide
269


OSPF Limit on Number of Redistributed Routes
Feature Information for OSPF Limit on Number of Redistributed Routes

IP Routing: OSPF Configuration Guide
270
