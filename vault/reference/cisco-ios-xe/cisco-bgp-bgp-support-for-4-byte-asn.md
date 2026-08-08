---
title: "BGP Support for 4-byte ASN"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-support-for-4-byte-asn
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 6 BGP Support for 4-byte ASN The Cisco implementation of 4-byte autonomous system (AS) numbers uses asplain (65538, for example) as the default regular expression match and the output display format for AS numbers. However, you can configure 4-byte AS numbers in both the asplain format and the asdot format as described in RFC 5396. In addition, 4-byte ASN route distinguisher (RD) and rou"
---

# BGP Support for 4-byte ASN

CHAPTER

6

BGP Support for 4-byte ASN
The Cisco implementation of 4-byte autonomous system (AS) numbers uses asplain (65538, for example) as
the default regular expression match and the output display format for AS numbers. However, you can configure
4-byte AS numbers in both the asplain format and the asdot format as described in RFC 5396. In addition,
4-byte ASN route distinguisher (RD) and route target (RT) BGP support for 4-byte autonomous numbers is
added.
• Finding Feature Information, on page 169
• Information About BGP Support for 4-byte ASN, on page 169
• How to Configure BGP Support for 4-byte ASN, on page 172
• Configuration Examples for BGP Support for 4-byte ASN, on page 179
• Additional References for BGP Support for 4-byte ASN, on page 183
• Feature Information for BGP Support for 4-byte ASN, on page 184

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Support for 4-byte ASN
BGP Autonomous System Number Formats
Prior to January 2009, BGP autonomous system (AS) numbers that were allocated to companies were 2-octet
numbers in the range from 1 to 65535 as described in RFC 4271, A Border Gateway Protocol 4 (BGP-4).
Due to increased demand for AS numbers, the Internet Assigned Number Authority (IANA) started to allocate
four-octet AS numbers in the range from 65536 to 4294967295. RFC 5396, Textual Representation of
Autonomous System (AS) Numbers, documents three methods of representing AS numbers. Cisco has
implemented the following two methods:

IP Routing: BGP Configuration Guide
169


BGP Support for 4-byte ASN
BGP Autonomous System Number Formats

• Asplain—Decimal value notation where both 2-byte and 4-byte AS numbers are represented by their
decimal value. For example, 65526 is a 2-byte AS number and 234567 is a 4-byte AS number.
• Asdot—Autonomous system dot notation where 2-byte AS numbers are represented by their decimal
value and 4-byte AS numbers are represented by a dot notation. For example, 65526 is a 2-byte AS
number and 1.169031 is a 4-byte AS number (this is dot notation for the 234567 decimal number).
For details about the third method of representing autonomous system numbers, see RFC 5396.
Asdot Only Autonomous System Number Formatting
In Cisco IOS XE Release 2.3, the 4-octet (4-byte) AS numbers are entered and displayed only in asdot notation,
for example, 1.10 or 45000.64000. When using regular expressions to match 4-byte AS numbers the asdot
format includes a period, which is a special character in regular expressions. A backslash must be entered
before the period (for example, 1\.14) to ensure the regular expression match does not fail. The table below
shows the format in which 2-byte and 4-byte AS numbers are configured, matched in regular expressions,
and displayed in show command output in Cisco IOS images where only asdot formatting is available.
Table 15: Asdot Only 4-Byte AS Number Format

Format Configuration Format

Show Command Output and Regular Expression Match
Format

asdot

2-byte: 1 to 65535 4-byte: 1.0 to 65535.65535

2-byte: 1 to 65535 4-byte: 1.0 to
65535.65535

Asplain as Default AS Number Formatting
In Cisco IOS XE Release 2.4 and later releases, the Cisco implementation of 4-byte AS numbers uses asplain
as the default display format for AS numbers, but you can configure 4-byte AS numbers in both the asplain
and asdot format. In addition, the default format for matching 4-byte AS numbers in regular expressions is
asplain, so you must ensure that any regular expressions to match 4-byte AS numbers are written in the asplain
format. If you want to change the default show command output to display 4-byte autonomous system numbers
in the asdot format, use the bgp asnotation dot command under router configuration mode. When the asdot
format is enabled as the default, any regular expressions to match 4-byte AS numbers must be written using
the asdot format, or the regular expression match will fail. The tables below show that although you can
configure 4-byte AS numbers in either asplain or asdot format, only one format is used to display show
command output and control 4-byte AS number matching for regular expressions, and the default is asplain
format. To display 4-byte AS numbers in show command output and to control matching for regular expressions
in the asdot format, you must configure the bgp asnotation dot command. After enabling the bgp asnotation
dot command, a hard reset must be initiated for all BGP sessions by entering the clear ip bgp * command.

Note

If you are upgrading to an image that supports 4-byte AS numbers, you can still use 2-byte AS numbers. The
show command output and regular expression match are not changed and remain in asplain (decimal value)
format for 2-byte AS numbers regardless of the format configured for 4-byte AS numbers.

IP Routing: BGP Configuration Guide
170


BGP Support for 4-byte ASN
Cisco Implementation of 4-Byte Autonomous System Numbers

Table 16: Default Asplain 4-Byte AS Number Format

Format Configuration Format

Show Command Output and Regular Expression
Match Format

asplain 2-byte: 1 to 65535 4-byte: 65536 to
4294967295

2-byte: 1 to 65535 4-byte: 65536 to 4294967295

asdot

2-byte: 1 to 65535 4-byte: 1.0 to 65535.65535 2-byte: 1 to 65535 4-byte: 65536 to 4294967295

Table 17: Asdot 4-Byte AS Number Format

Format Configuration Format

Show Command Output and Regular Expression
Match Format

asplain 2-byte: 1 to 65535 4-byte: 65536 to
4294967295

2-byte: 1 to 65535 4-byte: 1.0 to 65535.65535

asdot

2-byte: 1 to 65535 4-byte: 1.0 to 65535.65535 2-byte: 1 to 65535 4-byte: 1.0 to 65535.65535

Reserved and Private AS Numbers
In Cisco IOS XE Release 2.3 and later releases, the Cisco implementation of BGP supports RFC 4893. RFC
4893 was developed to allow BGP to support a gradual transition from 2-byte AS numbers to 4-byte AS
numbers. A new reserved (private) AS number, 23456, was created by RFC 4893 and this number cannot be
configured as an AS number in the Cisco IOS CLI.
RFC 5398, Autonomous System (AS) Number Reservation for Documentation Use, describes new reserved
AS numbers for documentation purposes. Use of the reserved numbers allow configuration examples to be
accurately documented and avoids conflict with production networks if these configurations are literally
copied. The reserved numbers are documented in the IANA AS number registry. Reserved 2-byte AS numbers
are in the contiguous block, 64496 to 64511 and reserved 4-byte AS numbers are from 65536 to 65551
inclusive.
Private 2-byte AS numbers are still valid in the range from 64512 to 65534 with 65535 being reserved for
special use. Private AS numbers can be used for internal routing domains but must be translated for traffic
that is routed out to the Internet. BGP should not be configured to advertise private AS numbers to external
networks. Cisco IOS software does not remove private AS numbers from routing updates by default. We
recommend that ISPs filter private AS numbers.

Note

AS number assignment for public and private networks is governed by the IANA. For information about AS
numbers, including reserved number assignment, or to apply to register an AS number, see the following
URL: http://www.iana.org/.

Cisco Implementation of 4-Byte Autonomous System Numbers
In Cisco IOS XE Release 2.4 and later releases, the Cisco implementation of 4-byte autonomous system (AS)
numbers uses asplain—65538, for example—as the default regular expression match and output display format
for AS numbers, but you can configure 4-byte AS numbers in both the asplain format and the asdot format
as described in RFC 5396. To change the default regular expression match and output display of 4-byte AS

IP Routing: BGP Configuration Guide
171


BGP Support for 4-byte ASN
How to Configure BGP Support for 4-byte ASN

numbers to asdot format, use the bgp asnotation dot command followed by the clear ip bgp * command to
perform a hard reset of all current BGP sessions. For more details about 4-byte AS number formats, see the
“BGP Autonomous System Number Formats” section.
In Cisco IOS XE Release 2.3, the Cisco implementation of 4-byte AS numbers uses asdot—1.2, for example—as
the only configuration format, regular expression match, and output display, with no asplain support. For an
example of BGP peers in two autonomous systems using 4-byte numbers, see the figure below. To view a
configuration example of the configuration between three neighbor peers in separate 4-byte autonomous
systems configured using asdot notation, see the “Example: Configuring a BGP Routing Process and Peers
Using 4-Byte Autonomous System Numbers” section.
Cisco also supports RFC 4893, which was developed to allow BGP to support a gradual transition from 2-byte
AS numbers to 4-byte AS numbers. To ensure a smooth transition, we recommend that all BGP speakers
within an AS that is identified using a 4-byte AS number be upgraded to support 4-byte AS numbers.

Note

A new private AS number, 23456, was created by RFC 4893, and this number cannot be configured as an AS
number in the Cisco IOS CLI.
Figure 16: BGP Peers in Two Autonomous Systems Using 4-Byte Numbers

How to Configure BGP Support for 4-byte ASN
Configuring a BGP Routing Process and Peers Using 4-Byte Autonomous
System Numbers
Perform this task to configure a Border Gateway Protocol (BGP) routing process and BGP peers when the
BGP peers are located in an autonomous system (AS) that uses 4-byte AS numbers. The address family
configured here is the default IPv4 unicast address family, and the configuration is done at Router B in the
figure above (in the “Cisco Implementation of 4-Byte Autonomous System Numbers” section). The 4-byte
AS numbers in this task are formatted in the default asplain (decimal value) format; for example, Router B is
in AS number 65538 in the figure above. Remember to perform this task for any neighbor routers that are to
be BGP peers.

IP Routing: BGP Configuration Guide
172


BGP Support for 4-byte ASN
Configuring a BGP Routing Process and Peers Using 4-Byte Autonomous System Numbers

Before you begin

Note

By default, neighbors that are defined using the neighbor remote-as command in router configuration mode
exchange only IPv4 unicast address prefixes. To exchange other address prefix types, such as IPv6 prefixes,
neighbors must also be activated using the neighbor activate command in address family configuration mode
for the other prefix types.

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
11.
12.

enable
configure terminal
router bgp autonomous-system-number
neighbor ip-address remote-as autonomous-system-number
Repeat Step 4 to define other BGP neighbors, as required.
address-family ipv4 [unicast | multicast | vrf vrf-name]
neighbor ip-address activate
Repeat Step 7 to activate other BGP neighbors, as required.
network network-number [mask network-mask] [route-map route-map-name]
end
show ip bgp [network] [network-mask]
show ip bgp summary

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

router bgp autonomous-system-number
Example:
Device(config)# router bgp 65538

Step 4

neighbor ip-address remote-as
autonomous-system-number
Example:

Enters router configuration mode for the specified routing
process.
• In this example, the 4-byte AS number, 65538, is
defined in asplain notation.
Adds the IP address of the neighbor in the specified AS to
the IPv4 multiprotocol BGP neighbor table of the local
device.
• In this example, the 4-byte AS number, 65536, is
defined in asplain notation.

IP Routing: BGP Configuration Guide
173


BGP Support for 4-byte ASN
Configuring a BGP Routing Process and Peers Using 4-Byte Autonomous System Numbers

Command or Action

Purpose

Device(config-router)# neighbor 192.168.1.2
remote-as 65536

Step 5

Repeat Step 4 to define other BGP neighbors, as required. --

Step 6

address-family ipv4 [unicast | multicast | vrf vrf-name] Specifies the IPv4 address family and enters address family
configuration mode.
Example:
• The unicast keyword specifies the IPv4 unicast
Device(config-router)# address-family ipv4 unicast
address family. By default, the device is placed in
configuration mode for the IPv4 unicast address
family if the unicast keyword is not specified with
the address-family ipv4 command.
• The multicast keyword specifies IPv4 multicast
address prefixes.
• The vrf keyword and vrf-name argument specify the
name of the virtual routing and forwarding (VRF)
instance to associate with subsequent IPv4 address
family configuration mode commands.

Step 7

neighbor ip-address activate
Example:

Enables the neighbor to exchange prefixes for the IPv4
unicast address family with the local device.

Device(config-router-af)# neighbor 192.168.1.2
activate

Step 8

Repeat Step 7 to activate other BGP neighbors, as required. --

Step 9

network network-number [mask network-mask]
[route-map route-map-name]
Example:
Device(config-router-af)# network 172.17.1.0 mask
255.255.255.0

Step 10

end
Example:

(Optional) Specifies a network as local to this AS and adds
it to the BGP routing table.
• For exterior protocols the network command controls
which networks are advertised. Interior protocols use
the network command to determine where to send
updates.
Exits address family configuration mode and returns to
privileged EXEC mode.

Device(config-router-af)# end

Step 11

show ip bgp [network] [network-mask]

(Optional) Displays the entries in the BGP routing table.

Example:

Note

Device# show ip bgp 10.1.1.0

IP Routing: BGP Configuration Guide
174

Only the syntax applicable to this task is used
in this example. For more details, see the Cisco
IOS IP Routing: BGP Command Reference.


BGP Support for 4-byte ASN
Troubleshooting Tips

Step 12

Command or Action

Purpose

show ip bgp summary

(Optional) Displays the status of all BGP connections.

Example:
Device# show ip bgp summary

Examples
The following output from the show ip bgp command at Router B shows the BGP routing table entry
for network 10.1.1.0 learned from the BGP neighbor at 192.168.1.2 in Router A in the figure above
with its 4-byte AS number of 65536 displayed in the default asplain format.
RouterB# show ip bgp 10.1.1.0
BGP routing table entry for 10.1.1.0/24, version 2
Paths: (1 available, best #1)
Advertised to update-groups:
2
65536
192.168.1.2 from 192.168.1.2 (10.1.1.99)
Origin IGP, metric 0, localpref 100, valid, external, best

The following output from the show ip bgp summary command shows the 4-byte AS number 65536
for the BGP neighbor 192.168.1.2 of Router A in the figure above after this task has been configured
on Router B:
RouterB# show ip bgp summary
BGP router identifier 172.17.1.99, local AS number 65538
BGP table version is 3, main routing table version 3
2 network entries using 234 bytes of memory
2 path entries using 104 bytes of memory
3/2 BGP path/bestpath attribute entries using 444 bytes of memory
1 BGP AS-PATH entries using 24 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 806 total bytes of memory
BGP activity 2/0 prefixes, 2/0 paths, scan interval 60 secs
Neighbor
V
AS MsgRcvd MsgSent
TblVer InQ OutQ Up/Down
192.168.1.2
4
65536
6
6
3
0
0 00:01:33

Stated
1

Troubleshooting Tips
Use the ping command to verify basic network connectivity between the BGP devices.

Modifying the Default Output and Regular Expression Match Format for 4-Byte
Autonomous System Numbers
Perform this task to modify the default output format for 4-byte autonomous system (AS) numbers from
asplain format to asdot notation format. The show ip bgp summary command is used to display the changes
in output format for the 4-byte AS numbers.

IP Routing: BGP Configuration Guide
175


BGP Support for 4-byte ASN
Modifying the Default Output and Regular Expression Match Format for 4-Byte Autonomous System Numbers

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
11.
12.
13.
14.

enable
show ip bgp summary
configure terminal
router bgp autonomous-system-number
bgp asnotation dot
end
clear ip bgp *
show ip bgp summary
show ip bgp regexp regexp
configure terminal
router bgp autonomous-system-number
no bgp asnotation dot
end
clear ip bgp *

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

show ip bgp summary
Example:

Displays the status of all Border Gateway Protocol (BGP)
connections.

Device# show ip bgp summary

Step 3

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 4

router bgp autonomous-system-number
Example:
Device(config)# router bgp 65538

Step 5

bgp asnotation dot
Example:

Enters router configuration mode for the specified routing
process.
• In this example, the 4-byte AS number, 65538, is
defined in asplain notation.
Changes the default output format of BGP 4-byte AS
numbers from asplain (decimal values) to dot notation.
Note

Device(config-router)# bgp asnotation dot

IP Routing: BGP Configuration Guide
176

4-byte AS numbers can be configured using
either asplain format or asdot format. This
command affects only the output displayed for
show commands or the matching of regular
expressions.


BGP Support for 4-byte ASN
Modifying the Default Output and Regular Expression Match Format for 4-Byte Autonomous System Numbers

Step 6

Command or Action

Purpose

end

Exits address family configuration mode and returns to
privileged EXEC mode.

Example:
Device(config-router)# end

Step 7

clear ip bgp *
Example:
Device# clear ip bgp *

Clears and resets all current BGP sessions.
• In this example, a hard reset is performed to ensure
that the 4-byte AS number format change is reflected
in all BGP sessions.
Note

Step 8

show ip bgp summary

Only the syntax applicable to this task is used
in this example. For more details, see the Cisco
IOS IP Routing: BGP Command Reference.

Displays the status of all BGP connections.

Example:
Device# show ip bgp summary

Step 9

show ip bgp regexp regexp
Example:

Displays routes that match the AS path regular expression.
• In this example, a regular expression to match a
4-byte AS path is configured using asdot format.

Device# show ip bgp regexp ^1\.0$

Step 10

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 11

router bgp autonomous-system-number
Example:
Device(config)# router bgp 65538

Step 12

no bgp asnotation dot
Example:

Enters router configuration mode for the specified routing
process.
• In this example, the 4-byte AS number, 65538, is
defined in asplain notation.
Resets the default output format of BGP 4-byte AS
numbers back to asplain (decimal values).
Note

Device(config-router)# no bgp asnotation dot

Step 13

end
Example:

4-byte AS numbers can be configured using
either asplain format or asdot format. This
command affects only the output displayed for
show commands or the matching of regular
expressions.

Exits router configuration mode and returns to privileged
EXEC mode.

Device(config-router)# end

IP Routing: BGP Configuration Guide
177


BGP Support for 4-byte ASN
Modifying the Default Output and Regular Expression Match Format for 4-Byte Autonomous System Numbers

Step 14

Command or Action

Purpose

clear ip bgp *

Clears and resets all current BGP sessions.

Example:
Device# clear ip bgp *

• In this example, a hard reset is performed to ensure
that the 4-byte AS number format change is reflected
in all BGP sessions.
Note

Only the syntax applicable to this task is used
in this example. For more details, see the Cisco
IOS IP Routing: BGP Command Reference.

Examples
The following output from the show ip bgp summary command shows the default asplain format
of the 4-byte AS numbers. Note the asplain format of the 4-byte AS numbers, 65536 and 65550.
Router# show ip bgp summary
BGP router identifier 172.17.1.99, local AS number 65538
BGP table version is 1, main routing table version 1
Neighbor
V
AS MsgRcvd MsgSent
TblVer InQ OutQ Up/Down
192.168.1.2
4
65536
7
7
1
0
0 00:03:04
192.168.3.2
4
65550
4
4
1
0
0 00:00:15

Statd
0
0

After the bgp asnotation dot command is configured (followed by the clear ip bgp * command to
perform a hard reset of all current BGP sessions), the output is converted to asdot notation format
as shown in the following output from the show ip bgp summary command. Note the asdot format
of the 4-byte AS numbers, 1.0 and 1.14 (these are the asdot conversions of the 65536 and 65550 AS
numbers.
Router# show ip bgp summary
BGP router identifier 172.17.1.99, local AS number 1.2
BGP table version is 1, main routing table version 1
Neighbor
V
AS MsgRcvd MsgSent
TblVer
192.168.1.2
4
1.0
9
9
1
192.168.3.2
4
1.14
6
6
1

InQ OutQ Up/Down
0
0 00:04:13
0
0 00:01:24

Statd
0
0

After the bgp asnotation dot command is configured (followed by the clear ip bgp * command to
perform a hard reset of all current BGP sessions), the regular expression match format for 4-byte AS
paths is changed to asdot notation format. Although a 4-byte AS number can be configured in a
regular expression using either asplain format or asdot format, only 4-byte AS numbers configured
using the current default format are matched. In the first example below, the show ip bgp regexp
command is configured with a 4-byte AS number in asplain format. The match fails because the
default format is currently asdot format and there is no output. In the second example using asdot
format, the match passes and the information about the 4-byte AS path is shown using the asdot
notation.

Note

The asdot notation uses a period, which is a special character in Cisco regular expressions. To remove
the special meaning, use a backslash before the period.

IP Routing: BGP Configuration Guide
178


BGP Support for 4-byte ASN
Configuration Examples for BGP Support for 4-byte ASN

Router# show ip bgp regexp ^65536$
Router# show ip bgp regexp ^1\.0$
BGP table version is 2, local router ID is 172.17.1.99
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete
Network
Next Hop
Metric LocPrf Weight Path
*> 10.1.1.0/24
192.168.1.2
0
0 1.0 i

Configuration Examples for BGP Support for 4-byte ASN
Examples: Configuring a BGP Routing Process and Peers Using 4-Byte
Autonomous System Numbers
Asplain Format
The following example shows the configuration for Router A, Router B, and Router E in the figure below
with a Border Gateway Protocol (BGP) process configured between three neighbor peers (at Router A, at
Router B, and at Router E) in separate 4-byte autonomous systems configured using asplain notation. IPv4
unicast routes are exchanged with all peers.
Figure 17: BGP Peers Using 4-Byte Autonomous System Numbers in Asplain Format

Router A
router bgp 65536
bgp router-id 10.1.1.99
no bgp default ipv4-unicast
bgp fast-external-fallover
bgp log-neighbor-changes
timers bgp 70 120
neighbor 192.168.1.1 remote-as 65538
!
address-family ipv4

IP Routing: BGP Configuration Guide
179


BGP Support for 4-byte ASN
Examples: Configuring a BGP Routing Process and Peers Using 4-Byte Autonomous System Numbers

neighbor 192.168.1.1 activate
no auto-summary
no synchronization
network 10.1.1.0 mask 255.255.255.0
exit-address-family

Router B
router bgp 65538
bgp router-id 172.17.1.99
no bgp default ipv4-unicast
bgp fast-external-fallover
bgp log-neighbor-changes
timers bgp 70 120
neighbor 192.168.1.2 remote-as 65536
neighbor 192.168.3.2 remote-as 65550
neighbor 192.168.3.2 description finance
!
address-family ipv4
neighbor 192.168.1.2 activate
neighbor 192.168.3.2 activate
no auto-summary
no synchronization
network 172.17.1.0 mask 255.255.255.0
exit-address-family

Router E
router bgp 65550
bgp router-id 10.2.2.99
no bgp default ipv4-unicast
bgp fast-external-fallover
bgp log-neighbor-changes
timers bgp 70 120
neighbor 192.168.3.1 remote-as 65538
!
address-family ipv4
neighbor 192.168.3.1 activate
no auto-summary
no synchronization
network 10.2.2.0 mask 255.255.255.0
exit-address-family

Asdot Format
The following example shows how to create the configuration for Router A, Router B, and Router E in the
figure below with a BGP process configured between three neighbor peers (at Router A, at Router B, and at
Router E) in separate 4-byte autonomous systems configured using the default asdot format. IPv4 unicast
routes are exchanged with all peers.

IP Routing: BGP Configuration Guide
180


BGP Support for 4-byte ASN
Examples: Configuring a BGP Routing Process and Peers Using 4-Byte Autonomous System Numbers

Figure 18: BGP Peers Using 4-Byte Autonomous System Numbers in Asdot Format

Router A
router bgp 1.0
bgp router-id 10.1.1.99
no bgp default ipv4-unicast
bgp fast-external-fallover
bgp log-neighbor-changes
timers bgp 70 120
neighbor 192.168.1.1 remote-as 1.2
!
address-family ipv4
neighbor 192.168.1.1 activate
no auto-summary
no synchronization
network 10.1.1.0 mask 255.255.255.0
exit-address-family

Router B
router bgp 1.2
bgp router-id 172.17.1.99
no bgp default ipv4-unicast
bgp fast-external-fallover
bgp log-neighbor-changes
timers bgp 70 120
neighbor 192.168.1.2 remote-as 1.0
neighbor 192.168.3.2 remote-as 1.14
neighbor 192.168.3.2 description finance
!
address-family ipv4
neighbor 192.168.1.2 activate
neighbor 192.168.3.2 activate
no auto-summary
no synchronization
network 172.17.1.0 mask 255.255.255.0
exit-address-family

Router E
router bgp 1.14

IP Routing: BGP Configuration Guide
181


BGP Support for 4-byte ASN
Examples: Configuring a VRF and Setting an Extended Community Using a BGP 4-Byte Autonomous System Number

bgp router-id 10.2.2.99
no bgp default ipv4-unicast
bgp fast-external-fallover
bgp log-neighbor-changes
timers bgp 70 120
neighbor 192.168.3.1 remote-as 1.2
!
address-family ipv4
neighbor 192.168.3.1 activate
no auto-summary
no synchronization
network 10.2.2.0 mask 255.255.255.0
exit-address-family

Examples: Configuring a VRF and Setting an Extended Community Using a BGP
4-Byte Autonomous System Number
Asplain Default Format in Cisco IOS Release 12.0(32)SY8, 12.0(33)S3, 12.2(33)SRE, 12.2(33)SXI1, and Later
Releases
The following example is available in Cisco IOS Release 12.0(32)SY8, 12.0(33)S3, 12.2(33)SRE, 12.2(33)XNE,
12.2(33)SXI1, and later releases and shows how to create a VRF with a route target that uses a 4-byte
autonomous system number, 65537, and how to set the route target to extended community value 65537:100
for routes that are permitted by the route map:
ip vrf vpn_red
rd 64500:100
route-target both 65537:100
exit
route-map red_map permit 10
set extcommunity rt 65537:100
end

After the configuration is completed, use the show route-map command to verify that the extended community
is set to the route target that contains the 4-byte autonomous system number of 65537:
RouterB# show route-map red_map
route-map red_map, permit, sequence 10
Match clauses:
Set clauses:
extended community RT:65537:100
Policy routing matches: 0 packets, 0 bytes

4-Byte Autonomous System Number RD Support
The following example shows how to create a VRF with a route distinguisher that contains a 4-byte AS number
65536, and a route target that contains a 4-byte autonomous system number, 65537:
ip vrf vpn_red
rd 65536:100
route-target both 65537:100
exit

After the configuration is completed, use the show vrf command to verify that the 4-byte AS number route
distinguisher is set to 65536:100:

IP Routing: BGP Configuration Guide
182


BGP Support for 4-byte ASN
Additional References for BGP Support for 4-byte ASN

RouterB# show vrf vpn_red
Current configuration : 36 bytes
vrf definition x
rd 65536:100
!

Asdot Default Format in Cisco IOS Release 12.0(32)S12, and 12.4(24)T
The following example is available in Cisco IOS Release 12.0(32)S12, and 12.4(24)T and shows how to create
a VRF with a route target that uses a 4-byte autonomous system number, 1.1, and how to set the route target
to the extended community value 1.1:100 for routes that are permitted by the route map.

Note

In Cisco IOS Release 12.0(32)SY8, 12.0(33)S3, 12.2(33)SXI1, and later releases, this example works if you
have configured asdot as the default display format using the bgp asnotation dot command.

ip vrf vpn_red
rd 64500:100
route-target both 1.1:100
exit
route-map red_map permit 10
set extcommunity rt 1.1:100
end

After the configuration is completed, use the show route-map command to verify that the extended community
is set to the route target that contains the 4-byte autonomous system number of 1.1.
RouterB# show route-map red_map
route-map red_map, permit, sequence 10
Match clauses:
Set clauses:
extended community RT:1.1:100
Policy routing matches: 0 packets, 0 bytes

Asdot Default Format for 4-Byte Autonomous System Number RD Support
The following example works if you have configured asdot as the default display format using the bgp
asnotation dot command:
ip vrf vpn_red
rd 1.0:100
route-target both 1.1:100
exit

Additional References for BGP Support for 4-byte ASN
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

IP Routing: BGP Configuration Guide
183


BGP Support for 4-byte ASN
Feature Information for BGP Support for 4-byte ASN

Related Topic

Document Title

BGP commands

Cisco IOS IP Routing: BGP Command Reference

Standards and RFCs
Standard/RFC Title
RFC 4893

BGP Support for Four-octet AS Number Space

RFC 5396

Textual Representation of Autonomous System (AS) Numbers

RFC 5398

Autonomous System (AS) Number Reservation for Documentation Use

RFC 5668

4-Octet AS Specific BGP Extended Community

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

Feature Information for BGP Support for 4-byte ASN
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.

IP Routing: BGP Configuration Guide
184


BGP Support for 4-byte ASN
Feature Information for BGP Support for 4-byte ASN

Table 18: Feature Information for BGP Support for 4-byte ASN

Feature Name

Releases

Feature Information

BGP Support for 4-byte ASN

Cisco IOS XE Release 2.3

The BGP Support for 4-Byte ASN
feature introduced support for
4-byte autonomous system
numbers.

Cisco IOS XE Release 2.4
Cisco IOS XE Release 3.9S

In Cisco IOS XE Release 2.4 and
later releases, the Cisco
implementation of 4-byte
autonomous system numbers uses
asplain as the default regular
expression match and output
display format for autonomous
system numbers, but you can
configure 4-byte autonomous
system numbers in both the asplain
format and the asdot format as
described in RFC 5396. To change
the default regular expression
match and output display of 4-byte
autonomous system numbers to
asdot format, use the bgp
asnotation dot command.
The following commands were
introduced or modified: bgp
asnotation dot, bgp confederation
identifier, bgp confederation
peers, all clear ip bgpcommands
that configure an autonomous
system number, ip as-path
access-list, ip extcommunity-list,
match source-protocol, neighbor
local-as, neighbor remote-as,
redistribute (IP), router bgp,
route-target, set as-path, set
extcommunity, set origin, all show
ip bgp commands that display an
autonomous system number, and
show ip extcommunity-list.
BGP—4-Byte ASN RD and RT
Support

Cisco IOS XE Release 3.13S

The BGP Support for 4-Byte ASN
RD and RT support for 4-byte
autonomous system numbers was
added.

IP Routing: BGP Configuration Guide
185


BGP Support for 4-byte ASN
Feature Information for BGP Support for 4-byte ASN

IP Routing: BGP Configuration Guide
186
