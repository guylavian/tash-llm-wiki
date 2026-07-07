---
title: "OSPF Support for Unlimited Software VRFs per PE Router"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-support-for-unlimited-software-vrfs-per-pe-router
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 31 OSPF Support for Unlimited Software VRFs per PE Router In a Multiprotocol Label Switching--Virtual Private Network (MPLS-VPN) deployment, each VPN routing and forwarding instance (VRF) needs a separate Open Shortest Path First (OSPF) process when configured to run OSPF. The OSPF Support for Unlimited Software VRFs per Provider Edge (PE) Router feature addresses the scalability issue f"
---

# OSPF Support for Unlimited Software VRFs per PE Router

CHAPTER

31

OSPF Support for Unlimited Software VRFs per
PE Router
In a Multiprotocol Label Switching--Virtual Private Network (MPLS-VPN) deployment, each VPN routing
and forwarding instance (VRF) needs a separate Open Shortest Path First (OSPF) process when configured
to run OSPF. The OSPF Support for Unlimited Software VRFs per Provider Edge (PE) Router feature
addresses the scalability issue for OSPF VPNs by eliminating the OSPF VPN limit of 32 processes.
• Finding Feature Information, page 295
• Prerequisites for OSPF Support for Unlimited Software VRFs per PE Router, page 296
• Restrictions for OSPF Support for Unlimited Software VRFs per PE Router, page 296
• Information About OSPF Support for Unlimited Software VRFs per PE Router, page 296
• How to Configure OSPF Support for Unlimited Software VRFs per PE Router, page 297
• Configuration Examples for OSPF Support for Unlimited Software VRFs per PE Router, page 298
• Additional References, page 299
• Feature Information for OSPF Support for Unlimited Software VRFs per PE Router, page 300

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
295


OSPF Support for Unlimited Software VRFs per PE Router
Prerequisites for OSPF Support for Unlimited Software VRFs per PE Router

Prerequisites for OSPF Support for Unlimited Software VRFs
per PE Router
You must have OSPF configured in your network.

Restrictions for OSPF Support for Unlimited Software VRFs per
PE Router
Only 32 processes per VRF can be supported. For different VRF processes, there is no limit.

Information About OSPF Support for Unlimited Software VRFs
per PE Router
Before Cisco IOS Releases 12.3(4)T and 12.0(27)S, a separate OSPF process was necessary for each VRF
that receives VPN routes via OSPF. When VPNs are deployed, an MPLS Provider Edge (PE) router will be
running both multiprotocol Border Gateway Protocol (BGP) for VPN distribution, and Interior Gateway
Protocol (IGP) for PE-P connectivity. OSPF is commonly used as the IGP between a customer edge (CE)
router and a PE router. OSPF was not scalable in a VPN deployment because of the limit of 32 processes. By
default, one process is used for connected routes and another process is used for static routes; therefore only
28 processes can be created for VRFs.
The OSPF Support for Unlimited Software VRFs per Provider Edge Router feature allows for an approximate
range of 300 to 10,000 VRFs, depending on the particular platform and on the applications, processes, and
protocols that are currently running on the platform.

IP Routing: OSPF Configuration Guide
296


OSPF Support for Unlimited Software VRFs per PE Router
How to Configure OSPF Support for Unlimited Software VRFs per PE Router

How to Configure OSPF Support for Unlimited Software VRFs
per PE Router
Configuring Unlimited Software VRFs per PE Router
SUMMARY STEPS
1. enable
2. configure terminal
3. ip vrf vpn-name
4. exit
5. router ospf process-id [vrf vpn-name]
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

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

ip vrf vpn-name

Defines a VPN routing and forwarding (VRF) instance and enters
VRP configuration mode.

Example:
Router(config)# ip vrf crf-1

Step 4

exit

Returns to global configuration mode.

Example:
Router(config-vrf)# exit

Step 5

router ospf process-id [vrf vpn-name]

Enables OSPF routing.

IP Routing: OSPF Configuration Guide
297


OSPF Support for Unlimited Software VRFs per PE Router
Configuration Examples for OSPF Support for Unlimited Software VRFs per PE Router

Command or Action

Purpose
• The process-id argument identifies the OSPF process.

Example:
Router(config)# router ospf 1 vrf crf-1

• Use the vrf keyword and vpn-name argument to identify
the VPN already defined in Step 3.
Note

Step 6

You can now configure as many OSPF VRF processes
as needed. Repeat Steps 3-5 as needed.

Returns to privileged EXEC mode.

end
Example:
Router(config-router)# end

Step 7

show ip ospf [process-id]

Displays general information about OSPF routing processes.

Example:
Router# show ip ospf 1

Configuration Examples for OSPF Support for Unlimited Software
VRFs per PE Router
Example Configuring OSPF Support for Unlimited Software VRFs per PE Router
This example shows a basic OSPF configuration using the router ospf command to configure OSPF VRF
processes for the VRFs first, second, and third:
Router> enable
Router# configure terminal
Router(config)# ip vrf first
Router(config-vrf)# exit
Router(config)# ip vrf second
Router(config-vrf)# exit
Router(config)# ip vrf third
Router(config-vrf)# exit
Router(config)# router ospf 12 vrf first
Router(config-router)# exit
Router(config)# router ospf 13 vrf second
Router(config-router)# exit
Router(config)# router ospf 14 vrf third
Router(config)# end

IP Routing: OSPF Configuration Guide
298


OSPF Support for Unlimited Software VRFs per PE Router
Example Verifying OSPF Support for Unlimited Software VRFs per PE Router

Example Verifying OSPF Support for Unlimited Software VRFs per PE Router
This example illustrates the output from the show ip ospf command to verify that OSPF VRF process 12 has
been created for the VRF named first. The output that relates to the VRF first appears in bold.
Router# show ip ospf 12
main ID type 0x0005, value 0.0.0.100
Supports only single TOS(TOS0) routes
Supports opaque LSA
Supports Link-local Signaling (LLS)
Supports area transit capability
Connected to MPLS VPN Superbackbone, VRF first
It is an area border router
Initial SPF schedule delay 5000 msecs
Minimum hold time between two consecutive SPFs 10000 msecs
Maximum wait time between two consecutive SPFs 10000 msecs
Incremental-SPF disabled
Minimum LSA interval 5 secs
Minimum LSA arrival 1000 msecs
LSA group pacing timer 240 secs
Interface flood pacing timer 33 msecs
Retransmission pacing timer 66 msecs
Number of external LSA 0. Checksum Sum 0x0
Number of opaque AS LSA 0. Checksum Sum 0x0
Number of DCbitless external and opaque AS LSA 0
Number of DoNotAge external and opaque AS LSA 0
Number of areas in this router is 1. 1 normal 0 stub 0 nssa
Number of areas transit capable is 0
External flood list length 0
Area BACKBONE(0)
Number of interfaces in this area is 1
Area has no authentication
SPF algorithm last executed 00:00:15.204 ago
SPF algorithm executed 2 times
Area ranges are
Number of LSA 1. Checksum Sum 0xD9F3
Number of opaque link LSA 0. Checksum Sum 0x0
Number of DCbitless LSA 0
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0

Additional References
The following sections provide references related to the OSPF Support for Unlimited Software VRFs per
Provider Edge Router feature.
Related Documents
Related Topic

Document Title

Configuring OSPF

"Configuring OSPF"

Standards
Standard

Title

None

--

IP Routing: OSPF Configuration Guide
299


OSPF Support for Unlimited Software VRFs per PE Router
Feature Information for OSPF Support for Unlimited Software VRFs per PE Router

MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this
feature, and support for existing MIBs has not been
modified by this feature.

To locate and download MIBs for selected platforms,
Cisco IOS XE releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFC

Title

None

--

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

Feature Information for OSPF Support for Unlimited Software
VRFs per PE Router
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
300


OSPF Support for Unlimited Software VRFs per PE Router
Feature Information for OSPF Support for Unlimited Software VRFs per PE Router

Table 34: Feature Information for OSPF Support for Unlimited Software VRFs per Provider Edge Router

Feature Name

Releases

OSPF Support for Unlimited
Cisco IOS XE Release 2.1
Software VRFs per Provider Edge
Router

Feature Information
In a Multiprotocol Label
Switching--Virtual Private
Network (MPLS-VPN)
deployment, each VPN routing and
forwarding instance (VRF) needs
a separate Open Shortest Path First
(OSPF) process when configured
to run OSPF. The OSPF Support
for Unlimited Software VRFs per
Provider Edge Router feature
addresses the scalability issue for
OSPF VPNs by eliminating the
OSPF VPN limit of 32 processes.

IP Routing: OSPF Configuration Guide
301


OSPF Support for Unlimited Software VRFs per PE Router
Feature Information for OSPF Support for Unlimited Software VRFs per PE Router

IP Routing: OSPF Configuration Guide
302
