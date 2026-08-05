---
title: "OSPF MIB Support of RFC 1850 and Latest Extensions"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-mib-support-of-rfc-1850-and-latest-extensions
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 35 OSPF MIB Support of RFC 1850 and Latest Extensions The OSPF MIB Support of RFC 1850 and Latest Extensions feature introduces the capability for Simple Network Management Protocol (SNMP) monitoring on the Open Shortest Path First (OSPF) routing protocol. Users have an improved ability to constantly monitor the changing state of an OSPF network by use of MIB objects to gather informatio"
---

# OSPF MIB Support of RFC 1850 and Latest Extensions

CHAPTER

35

OSPF MIB Support of RFC 1850 and Latest
Extensions
The OSPF MIB Support of RFC 1850 and Latest Extensions feature introduces the capability for Simple
Network Management Protocol (SNMP) monitoring on the Open Shortest Path First (OSPF) routing protocol.
Users have an improved ability to constantly monitor the changing state of an OSPF network by use of MIB
objects to gather information relating to protocol parameters and trap notification objects that can signal the
occurrence of significant network events such as transition state changes. The protocol information collected
by the OSPF MIB objects and trap objects can be used to derive statistics that will help monitor and improve
overall network performance.
• Finding Feature Information, page 321
• Prerequisites for OSPF MIB Support of RFC 1850 and Latest Extensions, page 322
• Information About OSPF MIB Support of RFC 1850 and Latest Extensions, page 322
• How to Enable OSPF MIB Support of RFC 1850 and Latest Extensions, page 328
• Configuration Examples for OSPF MIB Support of RFC 1850 and Latest Extensions, page 333
• Where to Go Next, page 333
• Additional References, page 333
• Feature Information for OSPF MIB Support of RFC 1850 and Latest Extensions, page 334

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
321


OSPF MIB Support of RFC 1850 and Latest Extensions
Prerequisites for OSPF MIB Support of RFC 1850 and Latest Extensions

Prerequisites for OSPF MIB Support of RFC 1850 and Latest
Extensions
• OSPF must be configured on the router.
• Simple Network Management Protocol (SNMP) must be enabled on the router before notifications
(traps) can be configured or before SNMP GET operations can be performed.

Information About OSPF MIB Support of RFC 1850 and Latest
Extensions
The following sections contain information about MIB objects standardized as part of RFC 1850 and defined
in OSPF-MIB and OSPF-TRAP-MIB. In addition, extensions to RFC 1850 objects are described as defined
in the two Cisco private MIBs, CISCO-OSPF-MIB and CISCO-OSPF-TRAP-MIB.

OSPF MIB Changes to Support RFC 1850
OSPF MIB
This section describes the new MIB objects that are provided by RFC 1850 definitions. These OSPF MIB
definitions provide additional capacity that is not provided by the standard OSPF MIB that supported the
previous RFC 1253. To see a complete set of OSPF MIB objects, see the OSPF-MIB file.
The table below shows the new OSPF-MIB objects that are provided by RFC 1850 definitions. The objects
are listed in the order in which they appear within the OSPF-MIB file, per the tables that describe them.
Table 38: New OSPF-MIB Objects

OSPF-MIB Table
OspfAreaEntry table

New MIB Objects
• OspfAreaSummary
• OspfAreaStatus

OspfStubAreaEntry

OspfAreaRangeEntry

OspfHostEntry

IP Routing: OSPF Configuration Guide
322

• OspfStubMetricType

• OspfAreaRangeEffect

• OspfHostAreaID


OSPF MIB Support of RFC 1850 and Latest Extensions
OSPF MIB Changes to Support RFC 1850

OSPF-MIB Table
OspfIfEntry

New MIB Objects
• OspfIfStatus
• OspfIfMulticastForwarding
• OspfIfDemand
• OspfIfAuthType

OspfVirtIfEntry

OspfNbrEntry

• OspfVirtIfAuthType

• OspfNbmaNbrPermanence
• OspfNbrHelloSuppressed

OspfVirtNbrEntry

OspfExtLsdbEntry

• OspfVirtNbrHelloSuppressed

• OspfExtLsdbType
• OspfExtLsdbLsid
• OspfExtLsdbRouterId
• OspfExtLsdbSequence
• OspfExtLsdbAge
• OspfExtLsdbChecksum
• OspfExtLsdbAdvertisement

OspfAreaAggregateEntry

• OspfAreaAggregateAreaID
• OspfAreaAggregateLsdbType
• OspfAreaAggregateNet
• OspfAreaAggregateMask
• OspfAreaAggregateStatusospfSetTrap
• OspfAreaAggregateEffect

OSPF TRAP MIB
This section describes scalar objects and MIB objects that are provided to support RFC 1850.

IP Routing: OSPF Configuration Guide
323


OSPF MIB Support of RFC 1850 and Latest Extensions
OSPF MIB Changes to Support RFC 1850

The following scalar objects are added to OSPF-TRAP-MIB and are listed in the order in which they appear
in the OSPF-TRAP-MIB file:
• OspfExtLsdbLimit
• OspfMulticastExtensions
• OspfExitOverflowInterval
• OspfDemandExtensions
The ospfSetTrap control MIB object contains the OSPF trap MIB objects that enable and disable OSPF traps
in the IOS CLI. These OSPF trap MIB objects are provided by the RFC 1850 standard OSPF MIB. To learn
how to enable and disable the OSPF traps, see the How to Enable OSPF MIB Support of RFC 1850 and Latest
Extensions, on page 328.
The table below shows the OSPF trap MIB objects, listed in the order in which they appear within the
OSPF-TRAP-MIB file.
Table 39: New OSPF-TRAP-MIB Objects

OSPF Control MIB Object
ospfSetTrap

Trap MIB Objects
• ospfIfStateChange
• ospfVirtIfStateChange
• ospfNbrStateChange
• ospfVirtNbrState
• ospfIfConfigError
• ospfVirtIfConfigError
• ospfIfAuthFailure
• ospfVirtIfAuthFailure
• ospfIfRxBadPacket
• ospfVirtIfRxBadPacket
• ospfTxRetransmit
• ospfVirtIfTxRetransmit
• ospfOriginateLsa
• ospfMaxAgeLsa

CISCO OSPF MIB
This section describes scalar and Cisco-specific OSPF MIB objects that are provided as extensions to support
the RFC 1850 OSPF MIB definitions, to provide capability that the standard MIB cannot provide.
The following scalar objects are added to OSPF-OSPF-MIB:

IP Routing: OSPF Configuration Guide
324


OSPF MIB Support of RFC 1850 and Latest Extensions
OSPF MIB Changes to Support RFC 1850

• cospfRFC1583Compatibility
• cospfOpaqueLsaSupport
• cospfOpaqueASLsaCount
• cospfOpaqueASLsaCksumSum
For each of the following table entries, the new Cisco-specific MIB objects that are provided as extensions
to support the RFC 1850 OSPF MIB definitions are listed. To see the complete set of objects for the
Cisco-specific OSPF MIB, refer to the CISCO-OSPF-MIB file.
The table below shows the new CISCO-OSPF-MIB objects that are provided by RFC 1850 definitions. The
objects are listed in the order in which they appear within the CISCO-OSPF-MIB file, per the tables that
describe them.
Table 40: New CISCO-OSPF-MIB Objects

CISCO-OSPF-MIB Table
cospfAreaEntry

New MIB Objects
• cospfOpaqueAreaLsaCount
• cospfOpaqueAreaLsaCksumSum
• cospfAreaNssaTranslatorRole
• cospfAreaNssaTranslatorState
• cospfAreaNssaTranslatorEvents

cospfLsdbEntry

• cospfLsdbType
• cospfLsdbSequence
• cospfLsdbAge
• cospfLsdbChecksum
• cospfLsdbAdvertisement

cospfIfEntry

• cospfIfLsaCount
• cospfIfLsaCksumSum

cospfVirtIfEntry

• cospfVirtIfLsaCount
• cospfVirtIfLsaCksumSum

IP Routing: OSPF Configuration Guide
325


OSPF MIB Support of RFC 1850 and Latest Extensions
OSPF MIB Changes to Support RFC 1850

CISCO-OSPF-MIB Table
cospfLocalLsdbEntry

New MIB Objects
• cospfLocalLsdbIpAddress
• cospfLocalLsdbAddressLessIf
• cospfLocalLsdbType
• cospfLocalLsdbLsid
• cospfLocalLsdbRouterId
• cospfLocalLsdbSequence
• cospfLocalLsdbAge
• cospfLocalLsdbChecksum
• cospfLocalLsdbAdvertisement

cospfVirtLocalLsdbEntry

• cospfVirtLocalLsdbTransitArea
• cospfVirtLocalLsdbNeighbor
• cospfVirtLocalLsdbType
• cospfVirtLocalLsdbLsid
• cospfVirtLocalLsdbRouterId
• cospfVirtLocalLsdbSequence
• cospfVirtLocalLsdbAge
• cospfVirtLocalLsdbChecksum
• cospfVirtLocalLsdbAdvertisement

CISCO OSPF TRAP MIB
The cospfSetTrap MIB object represents trap events in CISCO-OSPF-TRAP-MIB. This is a bit map, where
the first bit represents the first trap. The following MIB objects are TRAP events that have been added to
support RFC 1850. To see a complete set of Cisco OSPF Trap MIB objects, see the CISCO-OSPF-TRAP-MIB
file.
The table below shows the trap events described within the cospfSetTrap MIB object in the CISCO-TRAP-MIB:
Table 41: CISCO-OSPF Trap Events

CISCO-OSPF-TRAP-MIB Trap Events

Trap Event Description

cospfIfConfigError

This trap is generated for mismatched MTU parameter
errors that occur when nonvirtual OSPF neighbors
are forming adjacencies.

IP Routing: OSPF Configuration Guide
326


OSPF MIB Support of RFC 1850 and Latest Extensions
Benefits of the OSPF MIB

CISCO-OSPF-TRAP-MIB Trap Events

Trap Event Description

cospfVirtIfConfigError

This trap is generated for mismatched MTU parameter
errors when virtual OSPF neighbors are forming
adjacencies.

cospfTxRetransmit

This trap is generated in the case of opaque LSAs
when packets are sent by a nonvirtual interface. An
opaque link-state advertisement (LSA) is used in
MPLS traffic engineering to distribute attributes such
as capacity and topology of links in a network. The
scope of this LSA can be confined to the local
network (Type 9, Link-Local), OSPF area (Type 20,
Area-Local), or autonomous system (Type 11, AS
scope). The information in an opaque LSA can be
used by an external application across the OSPF
network.

cospfVirtIfTxRetransmit

This trap is generated in the case of opaque LSAs
when packets are sent by a virtual interface.

cospfOriginateLsa

This trap is generated when a new opaque LSA is
originated by the router when a topology change has
occurred.

cospfMaxAgeLsa

The trap is generated in the case of opaque LSAs.

cospfNssaTranslatorStatusChange

The trap is generated if there is a change in the ability
of a router to translate OSPF type-7 LSAs into OSPF
type-5 LSAs.

For information about how to enable OSPF MIB traps, see the How to Enable OSPF MIB Support of RFC
1850 and Latest Extensions, on page 328.

Benefits of the OSPF MIB
The OSPF MIBs (OSPF-MIB and OSPF-TRAP-MIB) and Cisco private OSPF MIBs (CISCO-OSPF-MIB
and CISCO-OSPF-TRAP-MIB) allow network managers to more effectively monitor the OSPF routing
protocol through the addition of new table objects and trap notification objects that previously were not
supported by the RFC 1253 OSPF MIB.
New CLI commands have been added to enable SNMP notifications for OSPF MIB support objects,
Cisco-specific errors, retransmission and state-change traps. The SNMP notifications are provided for errors
and other significant event information for the OSPF network.

IP Routing: OSPF Configuration Guide
327


OSPF MIB Support of RFC 1850 and Latest Extensions
How to Enable OSPF MIB Support of RFC 1850 and Latest Extensions

How to Enable OSPF MIB Support of RFC 1850 and Latest
Extensions
Enabling OSPF MIB Support
Before You Begin
Before the OSPF MIB Support of RFC 1850 and Latest Extensions feature can be used, the SNMP server for
the router must be configured.

SUMMARY STEPS
1. enable
2. configure terminal
3. snmp-server community string1
4. snmp-server community string2

ro
rw

5. snmp-server host {hostname | ip-address} [vrf vrf-name] [traps | informs] [version {1 | 2c | 3 [auth |
noauth | priv]}] community-string [udp-port port] [notification-type]
6. snmp-server enable traps ospf
7. end

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.
• Enter your password if prompted.

Example:
Router> enable

Step 2

Enters global configuration mode.

configure terminal
Example:
Router# configure terminal

Step 3

snmp-server community string1

ro

Example:
Router(config)# snmp-server community public
ro

IP Routing: OSPF Configuration Guide
328

Enables read access to all objects in the MIB, but does not allow
access to the community strings.


OSPF MIB Support of RFC 1850 and Latest Extensions
Enabling OSPF MIB Support

Command or Action
Step 4

snmp-server community string2

Purpose
rw

Enables read and write access to all objects in the MIB, but does
not allow access to the community strings.

Example:
Router(config)# snmp-server community
private rw

Step 5

snmp-server host {hostname | ip-address} [vrf
vrf-name] [traps | informs] [version {1 | 2c | 3
[auth | noauth | priv]}] community-string
[udp-port port] [notification-type]
Example:
Router(config)# snmp-server host
172.20.2.162 version 2c public ospf

Step 6

snmp-server enable traps ospf

Specifies a recipient (target host) for SNMP notification operations.
• If no notification-type is specified, all enabled notifications
(traps or informs) will be sent to the specified host.
• If you want to send only the OSPF notifications to the
specified host, you can use the optional ospfkeyword as one
of the notification-types. (See the example.) Entering the
ospf keyword enables the ospfSetTrap trap control MIB
object.
Enables all SNMP notifications defined in the OSPF MIBs.
Note

Example:
Router(config)# snmp-server enable traps
ospf

Step 7

This step is required only if you wish to enable all OSPF
traps. When you enter the no snmp-server enable traps
ospf command, all OSPF traps will be disabled.

Ends your configuration session and exits global configuration
mode.

end
Example:
Router(config)# end

What to Do Next
If you did not want to enable all OSPF traps, follow the steps in the following section to selectively enable
one or more types of OSPF trap:

IP Routing: OSPF Configuration Guide
329


OSPF MIB Support of RFC 1850 and Latest Extensions
Enabling Specific OSPF Traps

Enabling Specific OSPF Traps
SUMMARY STEPS
1. enable
2. configure terminal
3. snmp-server enable traps ospf cisco-specific errors [config-error] [virt-config-error]
4. snmp-server enable traps ospf cisco-specific retransmit [packets] [virt-packets]
5. snmp-server enable traps ospf cisco-specific state-change [nssa-trans-change] [shamlink-state-change]
6. snmp-server enable traps ospf cisco-specific lsa [lsa-maxage] [lsa-originate]
7. snmp-server enable traps ospf errors [authentication-failure] [bad-packet] [config-error]
[virt-authentication-failure] [virt-config-error]
8. snmp-server enable traps ospf lsa [lsa-maxage] [lsa-originate]
9. snmp-server enable traps ospf rate-limit seconds trap-number
10. snmp-server enable traps ospf retransmit [packets] [virt-packets]
11. snmp-server enable traps ospf state-change [if-state-change] [neighbor-state-change]
[virtif-state-change] [virtneighbor-state-change]

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

snmp-server enable traps ospf cisco-specific errors
[config-error] [virt-config-error]
Example:
Router(config)# snmp-server enable traps ospf
cisco-specific errors config-error

Step 4

snmp-server enable traps ospf cisco-specific retransmit
[packets] [virt-packets]

IP Routing: OSPF Configuration Guide
330

Enables SNMP notifications for Cisco-specific OSPF
configuration mismatch errors.
• Entering the snmp-server enable traps ospf
cisco-specific errors command with the optional
virt-config-error keyword enables only the SNMP
notifications for configuration mismatch errors on
virtual interfaces.
Enables error traps for Cisco-specific OSPF errors that
involve re-sent packets.


OSPF MIB Support of RFC 1850 and Latest Extensions
Enabling Specific OSPF Traps

Command or Action
Example:
Router(config)# snmp-server enable traps ospf
cisco-specific retransmit packets virt-packets

Step 5

Purpose
• Entering the snmp-server enable traps ospf
cisco-specific retransmit command with the
optional virt-packetskeyword enables only the
SNMP notifications for packets that are re-sent on
virtual interfaces.

snmp-server enable traps ospf cisco-specific state-change Enables all error traps for Cisco-specific OSPF transition
state changes.
[nssa-trans-change] [shamlink-state-change]
Example:
Router(config)# snmp-server enable traps ospf
cisco-specific state-change

Step 6

snmp-server enable traps ospf cisco-specific lsa
[lsa-maxage] [lsa-originate]

Enables error traps for opaque LSAs.

Example:
Router(config)# snmp-server enable traps ospf
cisco-specific lsa

Step 7

snmp-server enable traps ospf errors
[authentication-failure] [bad-packet] [config-error]
[virt-authentication-failure] [virt-config-error]
Example:
Router(config)# snmp-server enable traps ospf errors
virt-config-error

Step 8

snmp-server enable traps ospf lsa [lsa-maxage]
[lsa-originate]

Enables error traps for OSPF configuration errors.
• Entering the snmp-server enable traps ospf errors
command with the optional
virt-config-errorkeyword enables only the SNMP
notifications for OSPF configuration errors on
virtual interfaces.
Enables error traps for OSPF LSA errors.

Example:
Router(config)# snmp-server enable traps ospf lsa

Step 9

snmp-server enable traps ospf rate-limit seconds
trap-number

Sets the rate limit for how many SNMP OSPF
notifications are sent in each OSPF SNMP notification
rate-limit window.

Example:
Router(config)# snmp-server enable traps ospf
rate-limit 20 20

Step 10

snmp-server enable traps ospf retransmit [packets]
[virt-packets]

Enables SNMP OSPF notifications for re-sent packets.

IP Routing: OSPF Configuration Guide
331


OSPF MIB Support of RFC 1850 and Latest Extensions
Verifying OSPF MIB Traps on the Router

Command or Action

Purpose

Example:
Router(config)# snmp-server enable traps ospf
retransmit

Step 11

Enables SNMP OSPF notifications for OSPF transition
state changes.

snmp-server enable traps ospf state-change
[if-state-change] [neighbor-state-change]
[virtif-state-change] [virtneighbor-state-change]
Example:
Router(config)# snmp-server enable traps ospf
state-change

Verifying OSPF MIB Traps on the Router
SUMMARY STEPS
1. enable
2. show running-config [options]

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

show running-config [options]
Example:
Router# show running-config | include
traps

IP Routing: OSPF Configuration Guide
332

Displays the contents of the currently running configuration file
and includes information about enabled traps.
• Verifies which traps are enabled.


OSPF MIB Support of RFC 1850 and Latest Extensions
Configuration Examples for OSPF MIB Support of RFC 1850 and Latest Extensions

Configuration Examples for OSPF MIB Support of RFC 1850 and
Latest Extensions
Example Enabling and Verifying OSPF MIB Support Traps
The following example enables all OSPF traps.
Router# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)# snmp-server enable traps ospf
Router(config)# end

The show running-config command is entered to verify that the traps are enabled:
Router# show running-config | include traps
snmp-server enable traps ospf

Where to Go Next
For more information about SNMP and SNMP operations, see the "Configuring SNMP Support" chapter of
the Cisco IOS XE Network Management Configuration Guide, Release 2 .

Additional References
The following sections provide references related to the Area Command in Interface Mode for OSPFv2 feature.
Related Documents
Related Topic

Document Title

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

OSPF configuration tasks

"Configuring OSPF" module

Standards
Standard

Title

No new or modified standards are supported by this -feature, and support for existing standards has not
been modified by this feature.

IP Routing: OSPF Configuration Guide
333


OSPF MIB Support of RFC 1850 and Latest Extensions
Feature Information for OSPF MIB Support of RFC 1850 and Latest Extensions

MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this
feature, and support for existing MIBs has not been
modified by this feature.

To locate and download MIBs for selected platforms,
Cisco IOS releases, and feature sets, use Cisco MIB
Locator found at the following URL:
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

Feature Information for OSPF MIB Support of RFC 1850 and Latest
Extensions
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
334


OSPF MIB Support of RFC 1850 and Latest Extensions
Feature Information for OSPF MIB Support of RFC 1850 and Latest Extensions

Table 42: Feature Information for OSPF MIB Support of RFC 1850 and Latest Extensions

Feature Name

Releases

Feature Information

OSPF MIB Support of RFC 1850 Cisco IOS XE Release 2.1
and Latest Extensions

IP Routing: OSPF Configuration Guide
335


OSPF MIB Support of RFC 1850 and Latest Extensions
Feature Information for OSPF MIB Support of RFC 1850 and Latest Extensions

Feature Name

Releases

Feature Information
The OSPF MIB Support of RFC
1850 and Latest Extensions feature
introduces the capability for Simple
Network Management Protocol
(SNMP) monitoring on the Open
Shortest Path First (OSPF) routing
protocol. Users have an improved
ability to constantly monitor the
changing state of an OSPF network
by use of MIB objects to gather
information relating to protocol
parameters and trap notification
objects that can signal the
occurrence of significant network
events such as transition state
changes. The protocol information
collected by the OSPF MIB objects
and trap objects can be used to
derive statistics that will help
monitor and improve overall
network performance.
The following commands are
introduced or modified in the
feature documented in this module:
• snmp-server enable traps
ospf
• snmp-server enable traps
ospf cisco-specific errors
• snmp-server enable traps
ospf cisco-specific lsa
• snmp-server enable traps
ospf cisco-specific
retransmit
• snmp-server enable traps
ospf cisco-specific
state-change
• snmp-server enable traps
ospf errors
• snmp-server enable traps
ospf lsa
• snmp-server enable traps
ospf rate-limit
• snmp-server enable traps
ospf retransmit

IP Routing: OSPF Configuration Guide
336


OSPF MIB Support of RFC 1850 and Latest Extensions
Feature Information for OSPF MIB Support of RFC 1850 and Latest Extensions

Feature Name

Releases

Feature Information
• snmp-server enable traps
ospf state-change

IP Routing: OSPF Configuration Guide
337


OSPF MIB Support of RFC 1850 and Latest Extensions
Feature Information for OSPF MIB Support of RFC 1850 and Latest Extensions

IP Routing: OSPF Configuration Guide
338
