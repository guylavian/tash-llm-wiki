---
title: "Default Passive Interfaces"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-default-passive-interfaces
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 11 Default Passive Interfaces The Default Passive Interfaces feature simplifies the configuration of distribution devices by allowing all interfaces to be set as passive by default. In ISPs and large enterprise networks, many distribution devices have more than 200 interfaces. Obtaining routing information from these interfaces requires configuration of the routing protocol on all interf"
---

# Default Passive Interfaces

CHAPTER

11

Default Passive Interfaces
The Default Passive Interfaces feature simplifies the configuration of distribution devices by allowing all
interfaces to be set as passive by default. In ISPs and large enterprise networks, many distribution devices
have more than 200 interfaces. Obtaining routing information from these interfaces requires configuration of
the routing protocol on all interfaces and manual configuration of the passive-interface command on interfaces
where adjacencies were not desired.
• Finding Feature Information, on page 131
• Information About Default Passive Interfaces, on page 131
• How to Configure Default Passive Interfaces, on page 132
• Configuration Examples for Default Passive Interfaces, on page 134
• Additional References, on page 135
• Feature Information for Default Passive Interfaces, on page 135

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Information About Default Passive Interfaces
Default Passive Interfaces
In large enterprise networks, many distribution devices have more than 200 interfaces. Before the introduction
of the Default Passive Interfaces feature, routing information could be obtained from these interfaces in these
ways:
• Configure a routing protocol such as Open Shortest Path First (OSPF) on the backbone interfaces and
redistribute connected interfaces.
• Configure a routing protocol on all interfaces and manually set most of them as passive.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
131


Default Passive Interfaces
Preventing Routing Updates Through an Interface

Network operators might not always be able to summarize type 5 link-state advertisements (LSAs) at the
device level where redistribution occurs, as in the first possibility. Thus, a large number of type 5 LSAs can
be flooded over the domain.
In the second possibility, large type 1 LSAs might be flooded over the domain. The Area Border Router (ABR)
creates type 3 LSAs, one for each type 1 LSA, and floods them to the backbone. You can, however, have
unique summarization at the ABR level, which injects only one summary route into the backbone, thereby
reducing the processing overhead.
Before the introduction of the Default Passive Interfaces feature, you could configure the routing protocol on
all interfaces and manually set the passive-interface router configuration command on interfaces where
adjacencies were not desired. But in some networks, this solution meant configuring 200 or more passive
interfaces. The Default Passive Interfaces feature solved this problem by allowing all interfaces to be set as
passive by default. You can set all interfaces as passive by default by using the passive-interface default
command and then configure individual interfaces where adjacencies are desired using the no passive-interface
command.
The Default Passive Interfaces feature simplifies the configuration of distribution devices and allows the
network administrator to obtain routing information from interfaces in ISPs and large enterprise networks.

Preventing Routing Updates Through an Interface
To prevent other devices on a local network from learning about routes dynamically, you can keep routing
update messages from being sent through a device interface. This feature applies to all IP-based routing
protocols except the Border Gateway Protocol (BGP).
Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS) behave somewhat
differently. In OSPF, the interface address that you specify as passive appears as a stub network in the OSPF
domain. OSPF routing information is neither sent nor received through the specified device interface. In IS-IS,
the specified IP addresses are advertised without actually running IS-IS on those interfaces.
To prevent routing updates through a specified interface, use the passive-interface type number command
in router configuration mode.

How to Configure Default Passive Interfaces
Configuring Default Passive Interfaces
Perform this task to set all interfaces on a device, in an Enhanced Interior Gateway Routing Protocol (EIGRP)
environment, as passive by default, and then activate only those interfaces where adjacencies are desired.
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
router eigrp {autonomous-system-number | virtual-instance-number}
passive-interface [default] [type number]
no passive-interface [default] [type number]
network network-address [options]
end

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
132


Default Passive Interfaces
Configuring Default Passive Interfaces

8. show ip eigrp interfaces
9. show ip interface
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

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

router eigrp {autonomous-system-number |
virtual-instance-number}
Example:

Configures an EIGRP process and enters router
configuration mode.
• autonomous-system-number—Autonomous system
number that identifies the services to the other EIGRP
address-family devices. It is also used to tag routing
information. The range is 1 to 65535.

Device(config)# router eigrp 1

• virtual-instance-number—EIGRP virtual instance
name. This name must be unique among all
address-family router processes on a single device, but
need not be unique among devices
Step 4

passive-interface [default] [type number]

Sets all interfaces as passive by default.

Example:
Device(config-router)# passive-interface default

Step 5

no passive-interface [default] [type number]

Activates only those interfaces that need adjacencies.

Example:
Device(config-router)# no passive-interface
gigabitethernet 0/0/0

Step 6

network network-address [options]

Specifies the list of networks to be advertised by routing
protocols.

Example:
Device(config-router)# network 192.0.2.0

Step 7

end
Example:

Exits router configuration mode and returns to privileged
EXEC mode.

Device(config-router)# end

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
133


Default Passive Interfaces
Configuration Examples for Default Passive Interfaces

Step 8

Command or Action

Purpose

show ip eigrp interfaces

Verifies whether interfaces on your network have been set
to passive.

Example:
Device# show ip eigrp interfaces

Step 9

show ip interface

Verifies whether interfaces you enabled are active.

Example:
Device# show ip interface

Configuration Examples for Default Passive Interfaces
Examples: Passive Interfaces Configuration for OSPF
In Open Shortest Path First (OSPF), hello packets are not sent on an interface that is specified as passive.
Hence, the device is not able to discover any neighbors, and none of the OSPF neighbors are able to see the
device on that network. In effect, this interface appears as a stub network to the OSPF domain. This
configuration is useful if you want to import routes associated with a connected network into the OSPF domain
without any OSPF activity on that interface.
The passive-interface router configuration command is typically used when the wildcard specification on
the network router configuration command configures more interfaces than is desirable. The following
configuration causes OSPF to run on all subnets of 172.18.0.0:
Device(config)# interface GigabitEthernet 0/0/0
Device(config-if)# ip address 172.18.1.1 255.255.255.0
Device(config-if)# exit
Device(config)# interface GigabitEthernet 1/0/0
Device(config-if)# ip address 172.18.2.1 255.255.255.0
Device(config-if)# exit
Device(config)# interface GigabitEthernet 2/0/0
Device(config-if)# ip address 172.18.3.1 255.255.255.0
Device(config-if)# exit
Device(config)# router ospf 1
Device(config-router)# network 172.18.0.0 0.0.255.255 area 0
Device(config-router)# exit

If you do not want OSPF to run on 172.18.3.0, enter the following commands:
Device(config)# router ospf 1
Device(config-router)# network 172.18.0.0 0.0.255.255 area 0
Device(config-router)# no passive-interface GigabitEthernet 2/0/0
Device(config-router)# exit

Example: Default Passive Interfaces Configuration for OSPF
The following example configures the network interfaces, sets all interfaces that are running Open Shortest
Path First (OSPF) as passive, and then enables serial interface 0/0/0:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
134


Default Passive Interfaces
Additional References

Device(config)# interface GigabitEthernet 0/0/0
Device(config-if)# ip address 172.19.64.38 255.255.255.0 secondary
Device(config-if)# ip address 172.19.232.70 255.255.255.240
Device(config-if)# no ip directed-broadcast
Device(config-if)# exit
Device(config)# interface Serial 0/0/0
Device(config-if)# ip address 172.24.101.14 255.255.255.252
Device(config-if)# no ip directed-broadcast
Device(config-if)# no ip mroute-cache
Device(config-if)# exit
Device(config)# interface TokenRing 0/0/0
Device(config-if)# ip address 172.20.10.4 255.255.255.0
Device(config-if)# no ip directed-broadcast
Device(config-if)# no ip mroute-cache
Device(config-if)# ring-speed 16
Device(config-if)# exit
Device(config)# router ospf 1
Device(config-router)# passive-interface default
Device(config-router)# no passive-interface Serial 0/0/0
Device(config-router)# network 172.16.10.0 0.0.0.255 area 0
Device(config-router)# network 172.19.232.0 0.0.0.255 area 4
Device(config-router)# network 172.24.101.0 0.0.0.255 area 4
Device(config-router)# end

Additional References
Related Documents
Related Topic

Document Title

IP routing protocol-independent commands Cisco IOS IP Routing: Protocol-Independent Command
Reference
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

Feature Information for Default Passive Interfaces
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
135


Default Passive Interfaces
Feature Information for Default Passive Interfaces

Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 11: Feature Information for Default Passive Interfaces

Feature Name

Releases

Default Passive Interfaces

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
136

Feature Information
In ISP and large enterprise
networks, many of the distribution
devices have more than 200
interfaces. Obtaining routing
information from these interfaces
required configuration of the
routing protocol on all interfaces
and manual configuration of the
passive-interface command on the
interfaces where adjacency was not
desired. The Default Passive
Interface feature simplifies the
configuration of distribution
devices by allowing all interfaces
to be set as passive by default using
a single passive-interface default
command, and then by configuring
individual interfaces where
adjacencies are desired using the
no passive-interface command.
