---
title: "SGT Based QoS"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-sgt-based-qos
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 14 SGT Based QoS The SGT Based QoS feature supports the application of security group for packet classification for user group and role based or device based QoS traffic routing. • Finding Feature Information, on page 151 • Prerequisites for SGT Based QoS, on page 151 • Restrictions for SGT Based QoS, on page 151 • Information About SGT Based QoS, on page 152 • How to Configure SGT Based"
---

# SGT Based QoS

CHAPTER

14

SGT Based QoS
The SGT Based QoS feature supports the application of security group for packet classification for user group
and role based or device based QoS traffic routing.
• Finding Feature Information, on page 151
• Prerequisites for SGT Based QoS, on page 151
• Restrictions for SGT Based QoS, on page 151
• Information About SGT Based QoS, on page 152
• How to Configure SGT Based QoS, on page 152
• Configuration Examples for SGT Based QoS, on page 155
• Additional References for SGT Based QoS, on page 156
• Feature Information for SGT Based QoS, on page 156

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for SGT Based QoS
• The user groups and devices used for SGT Based QoS configuration must be assigned to the appropriate
SGT groups. SGT definition and mapping can be done through Cisco ISE or through static SGT
classification on the network device.

Restrictions for SGT Based QoS
• The SGT Based QoS feature does not support application prioritization within a user group.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
151


SGT Based QoS
Information About SGT Based QoS

• The SGT Based QoS feature does not support combining match application or match protocol criteria
with the match sgt criteria within a policy.

Information About SGT Based QoS
SGT Based QoS
Security Group classification includes both Source and Destination Group, which is specified by source SGT
and DGT. The SGT Based QoS feature enables prioritized allocation of bandwidth and QoS policies for a
defined user group or device. The SGT Based QoS feature provides you the capability to assign multiple QoS
policies to an application or traffic type initiated by different user groups. Each user group is defined by a
unique SGT value and supports hierarchical and non-hierarchical QoS configuration. The SGT Based QoS
feature supports both user group and device based QoS service levels for SGT/DGT based packet classification.
The SGT Based QoS feature supports defining of user groups based on contextual information for QoS policy
prioritization.

How to Configure SGT Based QoS
Configuring User Group, Device, or Role Based QoS Policies
SUMMARY STEPS
1.
2.
3.
4.
5.
6.

enable
configure terminal
class-map class-map-name
match security-group source tag sgt-number
match security-group destination tag dgt-number
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

Step 3

class-map class-map-name
Example:

Specifies the class-map and enters class-map configuration
mode.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
152


SGT Based QoS
Configuring and Assigning Policy-Map to an Interface

Command or Action

Purpose

Device(config)# class-map c1

Step 4

match security-group source tag sgt-number

Configures the value for security-group source security tag.

Example:
Device(config-cmap)# match security-group source
tag 1000

Step 5

match security-group destination tag dgt-number
Example:

Configures the value for security-group destination security
tag.

Device(config-cmap)# match security-group
destination tag 2000

Step 6

Exits route-map configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-cmap)# end

Configuring and Assigning Policy-Map to an Interface
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
policy-map policy-map-name
class class-map-name
bandwidth percent number
set dscp codepoint value
end
interface type slot/subslot/port [. subinterface-number]
service-policy {input | output} policy-map-name
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

Step 3

policy-map policy-map-name
Example:

Specifies the policy-map and enters policy-map
configuration mode.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
153


SGT Based QoS
Displaying and Verifying SGT Based QoS Configuration

Command or Action

Purpose

Device(config)# policy-map p1

Step 4

class class-map-name

Specifies the class and enters class configuration mode.

Example:
Device(config-pmap)# class c1

Step 5

bandwidth percent number

Configures the value for bandwidth percent.

Example:
Device(config-pmap-c)# bandwidth percent 20

Step 6

set dscp codepoint value
Example:

Configures the Differentiated Services Code Point (DSCP)
value.

Device(config-pmap-c)# set dscp ef

Step 7

end
Example:

Exits policy-map class action configuration mode and
returns to privileged EXEC mode.

Device(config-pmap-c)# end

Step 8

interface type slot/subslot/port [. subinterface-number]
Example:

Specifies the interface information and enters interface
configuration mode.

Device(config)#interface gigabitEthernet0/0/0.1

Step 9

service-policy {input | output} policy-map-name

Assigns policy-map to the input of an interface.

Example:
Device(config-if)# service-policy input p1

Step 10

end
Example:

Exits interface configuration mode and returns to privileged
EXEC mode.

Device(config-if)# end

Displaying and Verifying SGT Based QoS Configuration
SUMMARY STEPS
1. enable
2. show class-map
3. debug cpl provisioning{api | db | errors | ttc}
DETAILED STEPS

Step 1

enable
Example:
Device> enable

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
154


SGT Based QoS
Configuration Examples for SGT Based QoS

Enables privileged EXEC mode.
• Enter your password if prompted.
Step 2

show class-map
Example:
Device# show class-map
Class Map match-any class-default (id 0)
Match any
Class Map match-all c1 (id 1)
Match security-group source tag 1000
Match security-group destination tag 2000

Displays class-map information.
Step 3

debug cpl provisioning{api | db | errors | ttc}
Example:
Device# debug cpl provisioning api
CPL Policy Provisioning Manager API calls debugging is on

Enables debugging for Call Processing Language (CPL) provisioning.

Configuration Examples for SGT Based QoS
Example: Configuring User Group, Device, or Role Based QoS Policies
The following example shows how to configure User Group, Device, or Role Based QoS Policies:
enable
configure terminal
class-map c4
match security-group source tag 7000
match security-group destination tag 8000
end
policy-map p5
class c4
bandwidth percent 50
set dscp ef
end
interface gigabitEthernet0/0/0.1
service-policy input p5

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
155


SGT Based QoS
Additional References for SGT Based QoS

Additional References for SGT Based QoS
Related Documents
Related Topic

Document Title

Cisco IOS IP Routing Protocol Independent
commands

Cisco IOS IP Routing Protocol Independent Command
Reference

Cisco TrustSec Overview

Understanding Cisco TrustSec

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

Feature Information for SGT Based QoS
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 15: Feature Information for SGT Based QoS

Feature Name
SGT Based
QoS

Releases Feature Information
The SGT Based QoS feature supports classification of packets based on Security
Group Tag (SGT) for grouping the traffic into user groups and devices to match
the defined QoS policies.
The following commands were introduced or modified: debug cpl provisioning,
class-map match security-group destination tag, match security-group source
tag, show class-map.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
156
