---
title: "OSPF Per-Interface Link-Local Signaling"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-per-interface-link-local-signaling
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 33 OSPF Per-Interface Link-Local Signaling The OSPF Per-Interface Link-Local Signaling feature allows you to selectively enable or disable Link-Local Signaling (LLS) for a specific interface regardless of the global (router level) setting that you have previously configured. • Finding Feature Information, page 307 • Information About OSPF Per-Interface Link-Local Signaling, page 307 • Ho"
---

# OSPF Per-Interface Link-Local Signaling

CHAPTER

33

OSPF Per-Interface Link-Local Signaling
The OSPF Per-Interface Link-Local Signaling feature allows you to selectively enable or disable Link-Local
Signaling (LLS) for a specific interface regardless of the global (router level) setting that you have previously
configured.
• Finding Feature Information, page 307
• Information About OSPF Per-Interface Link-Local Signaling, page 307
• How to Configure OSPF Per-Interface Link-Local Signaling, page 308
• Configuration Examples for OSPF Per-Interface Link-Local Signaling, page 309
• Additional References, page 310
• Feature Information for OSPF Per-Interface Link-Local Signaling, page 312

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPF Per-Interface Link-Local Signaling
LLS allows for the extension of existing OSPF packets in order to provide additional bit space. The additional
bit space enables greater information per packet exchange between OSPF neighbors. This functionality is
used, for example, by the OSPF Nonstop Forwarding (NSF) Awareness feature that allows customer premises
equipment (CPE) routers that are NSF-aware to help NSF-capable routers perform nonstop forwarding of
packets.
When LLS is enabled at the router level, it is automatically enabled for all interfaces. The OSPF Per-Interface
Link-Local Signaling feature allows you to selectively enable or disable LLS for a specific interface. You
may want to disable LLS on a per-interface basis depending on your network design. For example, disabling

IP Routing: OSPF Configuration Guide
307


OSPF Per-Interface Link-Local Signaling
How to Configure OSPF Per-Interface Link-Local Signaling

LLS on an interface that is connected to a non-Cisco device that may be noncompliant with RFC 2328 can
prevent problems with the forming of OSPF neighbors in the network.

How to Configure OSPF Per-Interface Link-Local Signaling
Turning Off LLS on a Per-Interface Basis
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type slot /port
4. ip address ip-address mask [secondary]
5. no ip directed-broadcast [access-list-number | extended access-list-number]
6. ip ospf message-digest-key key-id encryption-type md5 key
7. [no | default] ip ospf lls [disable]

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

interface type slot /port

Configures an interface type and enters interface
configuration mode.

Example:
Router(config)# interface gigabitethernet 1/1/0

Step 4

ip address ip-address mask [secondary]

Sets a primary or secondary IP address for an interface.

Example:
Router(config-if)# ip address 10.2.145.20
255.255.255.0

Step 5

no ip directed-broadcast [access-list-number | extended Drops directed broadcasts destined for the subnet to which
that interface is attached, rather than broadcasting them.
access-list-number]

IP Routing: OSPF Configuration Guide
308


OSPF Per-Interface Link-Local Signaling
Configuration Examples for OSPF Per-Interface Link-Local Signaling

Command or Action
Example:

Purpose
• The forwarding of IP directed broadcasts on
Ethernet interface 1/0 is disabled.

Router(config-if)# no ip directed-broadcast

Step 6

ip ospf message-digest-key key-id encryption-type md5 Enables OSPF Message Digest 5 (MD5) algorithm
authentication.
key
Example:
Router(config-if)# ip ospf message-digest-key 100
md5 testing

Step 7

[no | default] ip ospf lls [disable]

Disables LLS on an interface, regardless of the global
(router level) setting.

Example:
Router(config-if)# ip ospf lls disable

What to Do Next
To verify that LLS has been enabled or disabled for a specific interface, use the show ip ospf interface
command. See the "Example: Configuring and Verifying the OSPF Per-Interface Link-Local Signaling Feature"
section for an example of the information displayed.

Configuration Examples for OSPF Per-Interface Link-Local
Signaling
Example Configuring and Verifying OSPF Per-Interface Link-Local Signaling
In the following example, LLS has been enabled on GigabitEthernet interface 1/1/0 and disabled on
GigabitEthernet interface 2/1/0:
interface gigabitethernet1/1/0
ip address 10.2.145.2 255.255.255.0
no ip directed-broadcast
ip ospf message-digest-key 1 md5 testing
ip ospf lls
!
interface gigabitethernet2/1/0
ip address 10.1.145.2 255.255.0.0
no ip directed-broadcast
ip ospf message-digest-key 1 md5 testing
!
ip ospf lls disable
interface Ethernet3/0
ip address 10.3.145.2 255.255.255.0

IP Routing: OSPF Configuration Guide
309


OSPF Per-Interface Link-Local Signaling
Additional References

no ip directed-broadcast
!
router ospf 1
log-adjacency-changes detail
area 0 authentication message-digest
redistribute connected subnets
network 10.0.0.0 0.255.255.255 area 1
network 10.2.3.0 0.0.0.255 area 1

In the following example, the show ip ospf interface command has been entered to verify that LLS has been
enabled for GigabitEthernet interface 1/1/0 and disabled for GigabitEthernet interface 2/1/0:
Router# show ip ospf interface
GigabitEthernet1/1/0 is up, line protocol is up
Internet Address 10.2.145.2/24, Area 1
Process ID 1, Router ID 10.22.222.2, Network Type BROADCAST, Cost: 10
Transmit Delay is 1 sec, State BDR, Priority 1
Designated Router (ID) 10.2.2.3, Interface address 10.2.145.1
Backup Designated router (ID) 10.22.222.2, Interface address 10.2.145.2
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
oob-resync timeout 40
Hello due in 00:00:00
!
Supports Link-local Signaling (LLS)
Index 1/1, flood queue length 0
Next 0x0(0)/0x0(0)
Last flood scan length is 2, maximum is 8
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 10.2.2.3 (Designated Router)
Suppress hello for 0 neighbor(s)
GigabitEthernet2/1/0 is up, line protocol is up
Internet Address 10.1.145.2/16, Area 1
Process ID 1, Router ID 10.22.222.2, Network Type BROADCAST, Cost: 10
Transmit Delay is 1 sec, State BDR, Priority 1
Designated Router (ID) 10.2.2.3, Interface address 10.1.145.1
Backup Designated router (ID) 10.22.222.2, Interface address 10.1.145.2
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
oob-resync timeout 40
Hello due in 00:00:04
!
Does not support Link-local Signaling (LLS)
Index 2/2, flood queue length 0
Next 0x0(0)/0x0(0)
Last flood scan length is 2, maximum is 11
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 45.2.2.3 (Designated Router)
Suppress hello for 0 neighbor(s)
GigabitEthernet3/1/0 is up, line protocol is up
Internet Address 10.3.145.2/24, Area 1
Process ID 1, Router ID 10.22.222.2, Network Type BROADCAST, Cost: 10
Transmit Delay is 1 sec, State BDR, Priority 1
Designated Router (ID) 10.2.2.3, Interface address 10.3.145.1
Backup Designated router (ID) 10.22.222.2, Interface address 10.3.145.2
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
oob-resync timeout 40
Hello due in 00:00:07
!
Supports Link-local Signaling (LLS)
Index 3/3, flood queue length 0
Next 0x0(0)/0x0(0)
Last flood scan length is 2, maximum is 11
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 10.2.2.3 (Designated Router)
Suppress hello for 0 neighbor(s)

Additional References
The following sections provide references related to the OSPF Per-Interface Link-Local Signaling feature.

IP Routing: OSPF Configuration Guide
310


OSPF Per-Interface Link-Local Signaling
Additional References

Related Documents
Related Topic

Document Title

Configuring OSPF

"Configuring OSPF"

Configuring OSPF NSF Awareness

"Cisco Nonstop Forwarding"

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Cisco IOS master command list, all releases

Cisco IOS Master Command List, All Releases

Standards
Standard

Title

None

--

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

RFC 2328

OSPF Version 2

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
311


OSPF Per-Interface Link-Local Signaling
Feature Information for OSPF Per-Interface Link-Local Signaling

Feature Information for OSPF Per-Interface Link-Local Signaling
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 36: Feature Information for OSPF Per-Interface Link-Local Signaling

Feature Name

Releases

Feature Information

OSPF Per-Interface Link-Local
Signaling

Cisco IOS XE Release 2.1

The OSPF Per-Interface
Link-Local Signaling feature
allows you to selectively enable or
disable Link-Local Signaling (LLS)
for a specific interface regardless
of the global (router level) setting
that you have previously
configured.
The following commands are
introduced or modified in the
feature documented in this module:
• ip ospf lls

IP Routing: OSPF Configuration Guide
312
