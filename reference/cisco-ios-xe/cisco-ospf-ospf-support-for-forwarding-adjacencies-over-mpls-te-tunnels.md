---
title: "OSPF Support for Forwarding Adjacencies over MPLS TE Tunnels"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-support-for-forwarding-adjacencies-over-mpls-te-tunnels
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 42 OSPF Support for Forwarding Adjacencies over MPLS TE Tunnels The OSPF Support for Forwarding Adjacencies over MPLS Traffic Engineered Tunnels feature adds Open Shortest Path First (OSPF) support to the Multiprotocol Label Switching (MPLS) Traffic Engineering (TE) Forwarding Adjacency feature, which allows a network administrator to handle a traffic engineering, label-switched path (LS"
---

# OSPF Support for Forwarding Adjacencies over MPLS TE Tunnels

CHAPTER

42

OSPF Support for Forwarding Adjacencies over
MPLS TE Tunnels
The OSPF Support for Forwarding Adjacencies over MPLS Traffic Engineered Tunnels feature adds Open
Shortest Path First (OSPF) support to the Multiprotocol Label Switching (MPLS) Traffic Engineering (TE)
Forwarding Adjacency feature, which allows a network administrator to handle a traffic engineering,
label-switched path (LSP) tunnel as a link in an Interior Gateway Protocol (IGP) network based on the
shortest path first (SPF) algorithm. An OSPF forwarding adjacency can be created between routers in the
same area.
History for the OSPF Support for Forwarding Adjacencies over MPLS Traffic Engineered Tunnels Feature
Release

Modification

12.0(24)S

This feature was introduced.

12.2(25)S

This feature was integrated into Cisco IOS Release
12.2(25)S.

12.2(18)SXE

This feature was integrated into Cisco IOS Release
12.2(18)SXE.

12.2(27)SBC

This feature was integrated into Cisco IOS Release
12.2(27)SBC.

Cisco IOS XE Release 2.1

This feature was implemented on Cisco ASR 1000
series routers.

• Finding Feature Information, page 402
• Prerequisites for OSPF Forwarding Adjacency, page 402
• Information About OSPF Forwarding Adjacency, page 402
• How to Configure OSPF Forwarding Adjacency, page 402
• Configuration Examples for OSPF Forwarding Adjacency, page 405

IP Routing: OSPF Configuration Guide
401


OSPF Support for Forwarding Adjacencies over MPLS TE Tunnels
Finding Feature Information

• Additional References, page 407

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPF Forwarding Adjacency
• OSPF must be configured in your network.
• Cisco Express Forwarding (CEF) must be enabled.
• You should understand MPLS TE tunnels for forwarding adjacency as described in the " MPLS Traffic
Engineering Forwarding Adjacency" module.

Information About OSPF Forwarding Adjacency
OSPF includes MPLS TE tunnels in the OSPF link-state database in the same way that other links appear for
purposes of routing and forwarding traffic. When an MPLS TE tunnel is configured between networking
devices, that link is considered a forwarding adjacency. The user can assign a cost to the tunnel to indicate
the link’s preference. Other networking devices will see the tunnel as a link in addition to the physical link.

How to Configure OSPF Forwarding Adjacency
Configuring OSPF Forwarding Adjacency
Note

Configure a forwarding adjacency on two LSP tunnels bidirectionally, from A to B and B to A. Otherwise,
the forwarding adjacency is advertised, but not used in the IGP network.

IP Routing: OSPF Configuration Guide
402


OSPF Support for Forwarding Adjacencies over MPLS TE Tunnels
Configuring OSPF Forwarding Adjacency

SUMMARY STEPS
1. enable
2. configure terminal
3. ip cef distributed
4. mpls traffic-eng tunnels
5. interface loopback number
6. ip address ip-address mask
7. no shutdown
8. exit
9. interface tunnel number
10. tunnel mode mpls traffic-eng
11. tunnel mpls traffic-eng forwarding-adjacency {holdtime value}
12. ip ospf cost cost
13. exit
14. router ospf process-id
15. mpls traffic-eng router-id interface
16. mpls traffic-eng area number
17. end

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

ip cef distributed

Enables Cisco Express Forwarding (CEF).

Example:
Router(config)# ip cef distributed

Step 4

mpls traffic-eng tunnels

Enables MPLS traffic engineering tunnel signaling on a
device.

Example:
Router(config)# mpls traffic-eng tunnels

IP Routing: OSPF Configuration Guide
403


OSPF Support for Forwarding Adjacencies over MPLS TE Tunnels
Configuring OSPF Forwarding Adjacency

Step 5

Command or Action

Purpose

interface loopback number

Configures a loopback interface and enters interface
configuration mode.

Example:
Router(config)# interface loopback0

Step 6

ip address ip-address mask

• Set up a loopback interface with a 32-bit mask, enable
CEF, enable MPLS traffic engineering, and set up a
routing protocol (OSPF) for the MPLS network.
Configures the IP address and subnet mask of the loopback
interface.

Example:
Router(config-if)# ip address 10.1.1.1
255.255.255.255

Step 7

no shutdown

Enables the interface.

Example:
Router(config-if)# no shutdown

Step 8

exit

Exits interface configuration mode.

Example:
Router(config-if)# exit

Step 9

interface tunnel number

Designates a tunnel interface for the forwarding adjacency
and enters interface configuration mode.

Example:
Router(config)# interface tunnel 1

Step 10

tunnel mode mpls traffic-eng

Sets the mode of a tunnel to MPLS for traffic engineering.

Example:
Router(config-if)# tunnel mode mpls
traffic-eng

Step 11

tunnel mpls traffic-eng forwarding-adjacency
{holdtime value}
Example:
Router(config-if)# tunnel mpls traffic-eng
forwarding-adjacency holdtime 10000

Step 12

ip ospf cost cost
Example:
Router(config-if)# ip ospf cost 4

IP Routing: OSPF Configuration Guide
404

Advertises a TE tunnel as a link in an IGP network.
• The holdtime value keyword argument combination is
the time in milliseconds (ms) that a TE tunnel waits
after going down before informing the network. The
range is 0 to 4,294,967,295 ms. The default value is 0.
(Optional) Configures the cost metric for a tunnel interface
to be used as a forwarding adjacency.


OSPF Support for Forwarding Adjacencies over MPLS TE Tunnels
Configuration Examples for OSPF Forwarding Adjacency

Step 13

Command or Action

Purpose

exit

Exits interface configuration mode.

Example:
Router(config-if)# exit

Step 14

router ospf process-id

Configures an OSPF routing process and enters router
configuration mode.

Example:
Router(config)# router ospf 1

Step 15

mpls traffic-eng router-id interface

Specifies that the traffic engineering router identifier for the
node is the IP address associated with a given interface.

Example:
Router(config-router)# mpls traffic-eng
router-id ethernet 1/0

Step 16

mpls traffic-eng area number

Configures a router running OSPF MPLS so that it floods
traffic engineering for the indicated OSPF area.

Example:
Router(config-router)# mpls traffic-eng area
1

Step 17

Exits router configuration mode.

end
Example:
Router(config-router)# end

Configuration Examples for OSPF Forwarding Adjacency
Example OSPF Forwarding Adjacency
In the following example, the tunnel destination is the loopback interface on the other router. The router is
configured with OSPF TE extensions and it floods traffic engineering link-state advertisements (LSAs) in
OSPF area 0. The traffic engineering router identifier for the node is the IP address associated with Loopback
0. The last five lines of the example set up the routing protocol for the MPLS network, which is OSPF in this
case.

IP Routing: OSPF Configuration Guide
405


OSPF Support for Forwarding Adjacencies over MPLS TE Tunnels
Example OSPF Forwarding Adjacency

Note

Do not use the mpls traffic-eng autoroute announce command if you configure a forwarding adjacency
in the tunnel.
ip routing
ip cef distributed
mpls traffic-eng tunnels
!
interface Loopback0
ip address 127.0.0.1 255.255.255.255
no shutdown
!
interface Tunnel1
ip unnumbered Loopback0
no ip directed-broadcast
tunnel destination 10.1.1.1
tunnel mode mpls traffic-eng
tunnel mpls traffic-eng forwarding-adjacency holdtime 10000
ip ospf cost 4
tunnel mpls traffic-eng priority 2 2
tunnel mpls traffic-eng bandwidth 10
tunnel mpls traffic-eng path-option 2 dynamic
router ospf 5
log-adjacency-changes
network 10.1.1.1 0.0.0.0 area 0
mpls traffic-eng router-id loopback0
mpls traffic-eng area 0

When you look at the self-generated router LSA, you will see it as one of the links in router LSA (shown in
bold in the following output).
Router# show ip ospf database route self-originate
OSPF Router with ID (10.5.5.5) (Process ID 5)
Router Link States (Area 0)
LS age:332
Options:(No TOS-capability, DC)
LS Type:Router Links
Link State ID:10.5.5.5
Advertising Router:10.5.5.5
LS Seq Number:80000004
Checksum:0x1D24
Length:72
Number of Links:4
Link connected to another Router (point-to-point)
(Link ID) Neighboring Router ID:10.3.3.3
(Link Data) Router Interface address:0.0.0.23
Number of TOS metrics:0
TOS 0 Metrics:1562
Link connected to:a Transit Network
(Link ID) Designated Router address:172.16.0.1
(Link Data) Router Interface address:172.16.0.2
Number of TOS metrics:0
TOS 0 Metrics:10
Link connected to:a Transit Network
(Link ID) Designated Router address:172.16.0.3
(Link Data) Router Interface address:172.16.0.4
Number of TOS metrics:0
TOS 0 Metrics:10
Link connected to:a Stub Network
(Link ID) Network/subnet number:10.5.5.5
(Link Data) Network Mask:255.255.255.255
Number of TOS metrics:0
TOS 0 Metrics:1

IP Routing: OSPF Configuration Guide
406


OSPF Support for Forwarding Adjacencies over MPLS TE Tunnels
Additional References

Additional References
The following sections provide references related to OSPF Forwarding Adjacency.
Related Documents
Related Topic

Document Title

MPLS traffic engineering forwarding adjacency

MPLS Traffic Engineering Forwarding Adjacency

Configuring OSPF for MPLS traffic engineering

MPLS Traffic Engineering and Enhancements

MPLS Traffic Engineering - LSP Attributes

MPLS Traffic Engineering - LSP Attributes

Standards
Standards

Title

No new or modified standards are supported by this -feature, and support for existing standards has not
been modified by this feature.

MIBs
MIBs

MIBs Link

None

To locate and download MIBs for selected platforms,
Cisco IOS releases, and feature sets, use Cisco MIB
Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFCs

Title

No new or modified RFCs are supported by this
feature, and support for existing RFCs has not been
modified by this feature.

--

IP Routing: OSPF Configuration Guide
407


OSPF Support for Forwarding Adjacencies over MPLS TE Tunnels
Additional References

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

IP Routing: OSPF Configuration Guide
408
