---
title: "OSPFv2 Loop-Free Alternate Fast Reroute"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv2-loop-free-alternate-fast-reroute
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 46 OSPFv2 Loop-Free Alternate Fast Reroute The OSPFv2 Loop-Free Alternate Fast Reroute feature uses a precomputed alternate next hop to reduce failure reaction time when the primary next hop fails. It lets you configure a per-prefix loop-free alternate (LFA) path that redirects traffic to a next hop other than the primary neighbor. The forwarding decision is made and service is restored"
---

# OSPFv2 Loop-Free Alternate Fast Reroute

CHAPTER

46

OSPFv2 Loop-Free Alternate Fast Reroute
The OSPFv2 Loop-Free Alternate Fast Reroute feature uses a precomputed alternate next hop to reduce
failure reaction time when the primary next hop fails. It lets you configure a per-prefix loop-free alternate
(LFA) path that redirects traffic to a next hop other than the primary neighbor. The forwarding decision is
made and service is restored without other routers’ knowledge of the failure.
• Finding Feature Information, page 433
• Prerequisites for OSPFv2 Loop-Free Alternate Fast Reroute, page 433
• Restrictions for OSPFv2 Loop-Free Alternate Fast Reroute, page 434
• Information About OSPFv2 Loop-Free Alternate Fast Reroute, page 434
• How to Configure OSPFv2 Loop-Free Alternate Fast Reroute, page 436
• Configuration Examples for OSPFv2 Loop-Free Alternate Fast Reroute, page 442
• Additional References, page 443
• Feature Information for OSPFv2 Loop-Free Alternate Fast Reroute, page 445

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPFv2 Loop-Free Alternate Fast Reroute
Open Shortest Path First (OSPF) supports IP FRR only on platforms that support this feature in the forwarding
plane. See the Cisco Feature Navigator, http://www.cisco.com/go/cfn , for information on platform support.
An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
433


OSPFv2 Loop-Free Alternate Fast Reroute
Restrictions for OSPFv2 Loop-Free Alternate Fast Reroute

Restrictions for OSPFv2 Loop-Free Alternate Fast Reroute
The OSPFv2 Loop-Free Alternate Fast Reroute feature is not supported on routers that are virtual links
headends.
The OSPFv2 Loop-Free Alternate Fast Reroute feature is supported only in global VPN routing and forwarding
(VRF) OSPF instances.
You cannot configure a traffic engineering (TE) tunnel interface as a protected interface. Use the MPLS Traffic
Engineering--Fast Reroute Link and Node Protection feature to protect these tunnels. See the “MPLS Traffic
Engineering--Fast Reroute Link and Node Protection” section in the Cisco IOS XE Multiprotocol Label
Switching Configuration Guide for more information.
You can configure a TE tunnel interface in a repair path, but OSPF will not verify the tunnel’s placement; you
must ensure that it is not crossing the physical interface it is intended to protect.
Not all routes can have repair paths. Multipath primary routes might have repair paths for all, some, or no
primary paths, depending on network topology, the connectivity of the computing router, and the attributes
required of repair paths.

Information About OSPFv2 Loop-Free Alternate Fast Reroute
LFA Repair Paths
The figure below shows how the OSPFv2 Loop-Free Alternate Fast Reroute feature reroutes traffic if a link
fails. A protecting router precomputes per-prefix repair paths and installs them in the global Routing Information
Base (RIB). When the protected primary path fails, the protecting router diverts live traffic from the primary
path to the stored repair path, without other routers’ having to recompute network topology or even be aware
that the network topology has changed.

LFA Repair Path Attributes
When a primary path fails, many paths are possible repair candidates. The OSPFv2 Loop-Free Alternate Fast
Reroute feature default selection policy prioritizes attributes in the following order:
1 srlg

IP Routing: OSPF Configuration Guide
434


OSPFv2 Loop-Free Alternate Fast Reroute
LFA Repair Path Attributes

2 primary-path
3 interface-disjoint
4 lowest-metric
5 linecard-disjoint
6 node-protecting
7 broadcast-interface-disjoint
If the evaluation does not select any candidate, the repair path is selected by implicit load balancing. This
means that repair path selection varies depending on prefix.
You can use the show ip ospf fast-reroute command to display the current configuration.
You can use the fast-reroute tie-break command to configure one or more of the repair-path attributes
described in the following sections to select among the candidates:

Shared Risk Link Groups
A shared risk link group (SRLG) is a group of next-hop interfaces of repair and protected primary paths that
have a high likelihood of failing simultaneously. The OSPFv2 Loop-Free Alternate Fast Reroute feature
supports only SRLGs that are locally configured on the computing router. VLANs on a single physical interface
are an example of an SRLG. If the physical interface fails, all the VLAN interfaces will fail at the same time.
The default repair-path attributes might result in the primary path on one VLAN being protected by a repair
path over another VLAN. You can configure the srlg attribute to specify that LFA repair paths do not share
the same SRLG ID as the primary path. Use the srlg command to assign an interface to an SRLG.

Interface Protection
Point-to-point interfaces have no alternate next hop for rerouting if the primary gateway fails. You can set
the interface-disjoint attribute to prevent selection of such repair paths, thus protecting the interface.

Broadcast Interface Protection
LFA repair paths protect links when a repair path and a protected primary path use different next-hop interfaces.
However, on broadcast interfaces, if the LFA repair path is computed via the same interface as the primary
path, but their next-hop gateways are different, the node is protected but the link might not be. You can set
the broadcast-interface-disjoint attribute to specify that the repair path never crosses the broadcast network
the primary path points to; that is, it cannot use the interface and the broadcast network connected to it.
See “ Broadcast and Non-Broadcast Multi-Access (NBMA) Links ” in RFC 5286, Basic Specification for IP
Fast Reroute: Loop-Free Alternates for information on network topologies that require this tiebreaker.

Node Protection
The default repair-path attributes might not protect the router that is the next hop in a primary path. You can
configure the node-protecting attribute to specify that the repair path will bypass the primary-path gateway
router.

IP Routing: OSPF Configuration Guide
435


OSPFv2 Loop-Free Alternate Fast Reroute
Candidate Repair-Path Lists

Downstream Path
In the case of a high-level network failure or multiple simultaneous network failures, traffic sent over an
alternate path might loop until OSPF recomputes the primary paths. You can configure the downstream
attribute to specify that the metric of any repair path to the protected destination must be lower than that of
the protecting node to the destination. This might result in lost traffic but it prevents looping.

Line-Card Disjoint Interfaces
Line-card interfaces are similar to SRLGs because all interfaces on the same line card will fail at the same
time if there is a problem with the line card, for example, line card online insertion and removal (OIR). You
can configure the linecard-disjoint attribute to specify that LFA repair paths use different interfaces than those
on the primary-path line card.

Metric
An LFA repair path need not be the most efficient of the candidates. A high-cost repair path might be considered
more attractive if it provides protection against higher-level network failures. You can configure the metric
attribute to specify a repair-path policy that has the lowest metric.

Equal-Cost Multipath Primary Paths
Equal-cost multipath paths (ECMPs) found during the primary shortest path first (SPF) repair, might not be
desirable in network designs where traffic is known to exceed the capacity of any single link. You can configure
the primary-path attribute to specify an LFA repair path from the ECMP set, or the secondary-path attribute
to specify an LFA repair path that is not from the ECMP set.

Candidate Repair-Path Lists
When OSPF computes a repair path, it keeps in the local RIB only the best from among all the candidate
paths, in order to conserve memory. You can use the fast-reroute keep-all-paths command to create a list
of all the candidate repair paths that were considered. This information can be useful for troubleshooting but
it can greatly increase memory consumption so it should be reserved for testing and debugging.

How to Configure OSPFv2 Loop-Free Alternate Fast Reroute
Enabling Per-Prefix OSPFv2 Loop-Free Alternate Fast Reroute
Perform this task to enable per-prefix OSPFv2 Loop-Free Alternate Fast Reroute and select the prefix priority
in an OSPF area.

IP Routing: OSPF Configuration Guide
436


OSPFv2 Loop-Free Alternate Fast Reroute
Specifying Prefixes to Be Protected by LFA FRR

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. fast-reroute per-prefix enable prefix-priority priority-level
5. exit

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

Enables OSPF routing and enters router configuration mode.

Example:
Router(config)# router ospf 10

Step 4

fast-reroute per-prefix enable prefix-priority
priority-level
Example:
Router (config-router)# fast-reroute
per-prefix enable prefix-priority low

Step 5

Enables repair-path computation and selects the priority level
for repair paths.
• Low priority specifies that all prefixes have the same
eligibility for protection. High priority specifies that only
high-priority prefixes are protected.
Exits router configuration mode and returns to global
configuration mode.

exit
Example:
Router (config-router)# exit

Specifying Prefixes to Be Protected by LFA FRR
Perform this task to specify which prefixes will be protected by LFA FRR. Only prefixes specified in the
route map will be protected.

IP Routing: OSPF Configuration Guide
437


OSPFv2 Loop-Free Alternate Fast Reroute
Specifying Prefixes to Be Protected by LFA FRR

Note

Only the following three match keywords are recognized in the route map: match tag, match route-type,
and match ip address prefix-list.
>

SUMMARY STEPS
1. enable
2. configure terminal
3. route-map map-tag [permit | deny] [sequence-number]
4. match tag tag-name
5. exit
6. router ospf process-id
7. prefix-priority priority-level route-map map-tag
8. exit

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

route-map map-tag [permit | deny] [sequence-number] Enters route-map configuration mode and specifies the
map name.
Example:
Router(config)# route-map OSPF-PREFIX-PRIORITY

Step 4

match tag tag-name
Example:

Specifies the prefixes to be matched.
• Only prefixes that match the tag will be protected.

Router(config-route-map)# match tag 886

Step 5

exit
Example:
Router(config-route-map)# exit

IP Routing: OSPF Configuration Guide
438

Exits route-map configuration mode and returns to global
configuration mode.


OSPFv2 Loop-Free Alternate Fast Reroute
Configuring a Repair Path Selection Policy

Step 6

Command or Action

Purpose

router ospf process-id

Enables OSPF routing and enters router configuration
mode.

Example:
Router(config)# router ospf 10

Step 7

prefix-priority priority-level route-map map-tag

Sets the priority level for repair paths and specifies the
route map that defines the prefixes.

Example:
Router(config-router)# prefix-priority high
route-map OSPF-PREFIX-PRIORITY

Step 8

Exits router configuration mode and returns to global
configuration mode.

exit
Example:
Router(config-router)# exit

Configuring a Repair Path Selection Policy
Perform this task to configure a repair path selection policy, specifying a tiebreaking condition. See the LFA
Repair Path Attributes, on page 434 for information on tiebreaking attributes.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. fast-reroute per-prefix tie-break attribute

[required] index index-level

5. exit

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

IP Routing: OSPF Configuration Guide
439


OSPFv2 Loop-Free Alternate Fast Reroute
Creating a List of Repair Paths Considered

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router ospf process-id

Enables OSPF routing and enters router configuration
mode.

Example:
Router(config)# router ospf 10

Step 4

fast-reroute per-prefix tie-break attribute
[required] index index-level

Configures a repair path selection policy by specifying a
tiebreaking condition and setting its priority level.

Example:
Router(config-router)# fast-reroute per-prefix
tie-break srlg required index 10

Step 5

Exits router configuration mode and returns to global
configuration mode.

exit
Example:
Router(config-router)# exit

Creating a List of Repair Paths Considered
Perform this task to create a list of paths considered for LFA FRR.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. fast-reroute keep-all-paths
5. exit

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

IP Routing: OSPF Configuration Guide
440


OSPFv2 Loop-Free Alternate Fast Reroute
Prohibiting an Interface From Being Used as the Next Hop

Command or Action

Purpose
• Enter your password if prompted.

Example:
Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router ospf process-id

Enables OSPF routing and enters router configuration
mode.

Example:
Router(config)# router ospf 10

Step 4

fast-reroute keep-all-paths

Specifies creating a list of repair paths considered for LFA
FRR.

Example:
Router(config-router)# fast-reroute
keep-all-paths

Step 5

Exits router configuration mode and returns to global
configuration mode.

exit
Example:
Router(config-router)# exit

Prohibiting an Interface From Being Used as the Next Hop
Perform this task to prohibit an interface from being used as the next hop in a repair path.

SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. ip ospf fast-reroute per-prefix candidate disable
5. exit

IP Routing: OSPF Configuration Guide
441


OSPFv2 Loop-Free Alternate Fast Reroute
Configuration Examples for OSPFv2 Loop-Free Alternate Fast Reroute

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

Enters interface configuration mode for the interface
specified.

Example:
Router(config)# interface GigabitEthernet 0/0/0

Step 4

ip ospf fast-reroute per-prefix candidate disable

Prohibits the interface from being used as the next hop
in a repair path.

Example:
Router(config-if)# ip ospf fast-reroute
per-prefix candidate disable

Step 5

Exits interface configuration mode and returns to global
configuration mode.

exit
Example:
Router(config-if)# exit

Configuration Examples for OSPFv2 Loop-Free Alternate Fast
Reroute
Example Enabling Per-Prefix LFA IP FRR
The following example shows how to enable per-prefix OSPFv2 Loop-Free Alternate Fast Reroute and select
the prefix priority in an OSPF area:
Router(config)# router ospf 10
fast-reroute per-prefix enable prefix-priority low

IP Routing: OSPF Configuration Guide
442


OSPFv2 Loop-Free Alternate Fast Reroute
Example Specifying Prefix-Protection Priority

Example Specifying Prefix-Protection Priority
The following example shows how to specify which prefixes will be protected by LFA FRR:
Router(config)# router ospf 10
prefix-priority high route-map OSPF-PREFIX-PRIORITY
fast-reroute per-prefix enable prefix-priority high
network 192.0.2.1 255.255.255.0 area 0
route-map OSPF-PREFIX-PRIORITY permit 10
match tag 866

Example Configuring Repair-Path Selection Policy
The following example shows how to configure a repair-path selection policy that sets SRLG, line card failure
and downstream as tiebreaking attributes, and sets their priority indexes:
router ospf 10
fast-reroute per-prefix enable prefix-priority low
fast-reroute per-prefix tie-break srlg required index 10
fast-reroute per-prefix tie-break linecard-disjoint index 15
fast-reroute per-prefix tie-break downstream index 20
network 192.0.2.1 255.255.255.0 area 0

Example Auditing Repair-Path Selection
The following example shows how to keep a record of repair-path selection:
router ospf 10
fast-reroute per-prefix enable prefix-priority low
fast-reroute keep-all-paths
network 192.0.2.1 255.255.255.0 area 0

Example Prohibiting an Interface from Being a Protecting Interface
The following example shows how to prohibit an interface from being a protecting interface:
Router(config)# interface GigabitEthernet 0/0/0
ip addres
s 192.0.2.1 255.255.255.0
ip ospf fast-reroute per-prefix candidate disable

Additional References
The following sections provide references related to the OSPF RFC 3623 Graceful Restart feature.
Related Documents
Related Topic

Document Title

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

IP Routing: OSPF Configuration Guide
443


OSPFv2 Loop-Free Alternate Fast Reroute
Additional References

Related Topic

Document Title

OSPF configuration

Configuring OSPF

Cisco nonstop forwarding

Cisco Nonstop Forwarding

OSPFv3 Graceful Restart

‘OSPFv3 Graceful Restart’ module

Standards
Standard

Title

None

--

MIBs
MIB

MIBs Link

None

To locate and download MIBs for selected platforms,
Cisco IOS releases, and feature sets, use Cisco MIB
Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFC

Title

RFC 2328

OSPF Version 2

RFC 3623

Graceful OSPF Restart

Technical Assistance
Description

Link

The Cisco Support website provides extensive online http://www.cisco.com/techsupport
resources, including documentation and tools for
troubleshooting and resolving technical issues with
Cisco products and technologies. Access to most tools
on the Cisco Support website requires a Cisco.com
user ID and password. If you have a valid service
contract but do not have a user ID or password, you
can register on Cisco.com.

IP Routing: OSPF Configuration Guide
444


OSPFv2 Loop-Free Alternate Fast Reroute
Feature Information for OSPFv2 Loop-Free Alternate Fast Reroute

Feature Information for OSPFv2 Loop-Free Alternate Fast Reroute
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 52: Feature Information for OSPFv2 Loop-Free Alternate Fast Reroute

Feature Name

Releases

Feature Information

OSPFv2 Loop-Free Alternate Fast Cisco IOS XE Release 3.4S
Reroute

This feature uses a precomputed
alternate next hop to reduce failure
reaction time when the primary
next hop fails.
The following commands were
introduced or modified: debug ip
ospf fast-reroute, fast-reroute
keep-all-paths, fast-reroute
per-prefix (OSPF), fast-reroute
tie-break (OSPF), ip ospf
fast-reroute per-prefix,
prefix-priority, show ip ospf
fast-reroute, show ip ospf
interface, show ip ospf neighbor,
show ip ospf rib .

IP Routing: OSPF Configuration Guide
445


OSPFv2 Loop-Free Alternate Fast Reroute
Feature Information for OSPFv2 Loop-Free Alternate Fast Reroute

IP Routing: OSPF Configuration Guide
446
