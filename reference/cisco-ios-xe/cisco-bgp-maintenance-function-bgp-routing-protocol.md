---
title: "Maintenance Function: BGP Routing Protocol"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-maintenance-function-bgp-routing-protocol
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 86 Maintenance Function: BGP Routing Protocol From Cisco IOS XE Everest 16.4.1 release, the event trace functionality is supported for BGP. Event Trace provides the functionality to capture BGP traces by enabling the event trace using commands. You can disable the command if you do not want to log traces. When convergence happens and connection states are getting changed, the BGP traces"
---

# Maintenance Function: BGP Routing Protocol

CHAPTER

86

Maintenance Function: BGP Routing Protocol
From Cisco IOS XE Everest 16.4.1 release, the event trace functionality is supported for BGP. Event Trace
provides the functionality to capture BGP traces by enabling the event trace using commands. You can disable
the command if you do not want to log traces. When convergence happens and connection states are getting
changed, the BGP traces are logged into Event Trace infrastructure.
• Finding Feature Information, on page 1157
• Information About Maintenance Function: BGP Routing Protocol, on page 1157
• Configuring BGP Event Trace in Global Configuration Mode, on page 1158
• Configuring BGP Event Trace in EXEC Mode, on page 1159
• Verifying the BGP Event Traces, on page 1160
• Feature Information for Maintenance Function: BGP Routing Protocol, on page 1160

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

InformationAboutMaintenanceFunction:BGPRoutingProtocol
BGP Event trace supports the following functionalities:
• BGP Event Trace creates buffers for peer connection state change and updates event logging. The size
of the buffer is 100,000, which means 100,000 trace entries will be stored at a time. The buffer can be
resized by using configuration command and maximum size of the buffer can be extended till 1,000,000.
• These buffers are circular in nature, that is, if the buffer reaches the end then it starts logging from the
beginning. If "one-shot" is not configured, it continuously logs from the beginning.
• Considering the contribution is a small addition to performance, BGP event trace will be disabled by
default. It can be enabled by executing the enable command in EXEC mode.
• BGP Event Traces:

IP Routing: BGP Configuration Guide
1157


Maintenance Function: BGP Routing Protocol
Configuring BGP Event Trace in Global Configuration Mode

• Neighbor: All the peer events such as state changes, error handling, unrecognized/malformed packet
handling will be captured into this buffer.
• BGP logs the traces in binary format into corresponding buffers on runtime, which helps in logging the
trace efficiently. Use the monitor event-trace bgp neighbor command to print the traces in
human-readable format on the console. This command provides the functionality of dumping the event
traces into the file in binary or human-readable format as well.
• The show commands are provided with afi/safi/vrf/neighbor address filtering options to display the event
logs. Event Trace logging under different afi/safi/vrf is completely based on the different traces.

Configuring BGP Event Trace in Global Configuration Mode
BGP Event Trace provides the commands in global configuration and privileged EXEC mode for connection
state event traces. Use the following configuration steps to enable the event-traces for BGP. With this
configuration, BGP traces are enabled after the active/standby router is rebooted because of a crash or
switchover.
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
monitor event-trace bgp neighbor {dump-file filename | size entries}
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

monitor event-trace bgp neighbor {dump-file filename Enables event traces for BGP.
| size entries}
Use the no monitor event-trace bgp neighbor command
to disable the event traces.
Example:
Device(config)# monitor event-trace bgp neighbor
size 10

Step 4

end
Example:

IP Routing: BGP Configuration Guide
1158

• dump-file—Set the name of the trace dump file.
• size—Set the size of trace.
Exits global configuration mode and enters privileged EXEC
mode.


Maintenance Function: BGP Routing Protocol
Configuring BGP Event Trace in EXEC Mode

Command or Action

Purpose

Device(config)# end

Configuring BGP Event Trace in EXEC Mode
SUMMARY STEPS
1. enable
2. monitor event-trace bgp neighbor {clear | continuous | destroy-buffer | disable | dump filename |
enable | one-shot}
3. exit
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

monitor event-trace bgp neighbor {clear | continuous | Enables event traces for BGP.
destroy-buffer | disable | dump filename | enable |
Use the no monitor event-trace bgp neighbor command
one-shot}
to disable the event traces.
Example:
• clear--Clear the event trace buffer.
• continuous--Display the event traces getting logged
Device# monitor event-trace bgp neighbor enable
continuously on the console.
• destroy-buffer--Destroy buffer allocated for traces.
• disable--Disable the event trace functionality. This
command must be given on active and standby to
disable both nodes.
• dump filename--Dump all neighbor event traces into
file in binary or ASCII format.
• enable--Enable the event trace functionality. This
command must be given on active and standby to
enable both nodes.
• one-shot--Log the event trace only once. When the
buffer is full, the event-trace logging will stop.

Step 3

exit

Exits the privileged EXEC configuration mode.

Example:
Device# exit

IP Routing: BGP Configuration Guide
1159


Maintenance Function: BGP Routing Protocol
Verifying the BGP Event Traces

Verifying the BGP Event Traces
You can use the following show commands to browse through the event traces captured. These show commands
will filter the traces based on the AFI/SAFI/VRF/neighbor address and different combinations.
• show monitor event-trace bgp all
• show monitor event-trace bgp back
• show monitor event-trace bgp clock
• show monitor event-trace bgp from-boot
• show monitor event-trace bgp ipv4 {all | back | clock | flowspec | from-boot | latest | mdt | multicast
| mvpn | unicast}
• show monitor event-trace bgp ipv4 flowspec neighbors
• show monitor event-trace bgp ipv4 mdt vrf
• show monitor event-trace bgp ipv6 {all | back | clock | flowspec | from-boot | latest | multicast | mvpn
| unicast}
• show monitor event-trace bgp l2vpn {all | back | clock | evpn | from-boot | latest | vpls}
• show monitor event-trace bgp latest
• show monitor event-trace bgp neighbors
• show monitor event-trace bgp nsap
• show monitor event-trace bgp parameters
• show monitor event-trace bgp rtfilter
• show monitor event-trace bgp vpnv4 {all | back | clock | from-boot | latest | vrf}
• show monitor event-trace bgp vpnv6 {all | back | clock | flowspec | from-boot | latest | multicast |
unicast}

Feature Information for Maintenance Function: BGP Routing
Protocol
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 106: Feature Information for Maintenance Function: BGP Routing Protocol

Feature Name

Releases

Maintenance Function: Cisco IOS XE
BGP Routing Protocol Everest 16.4.1
Release

IP Routing: BGP Configuration Guide
1160

Feature Information
From Cisco IOS XE Everest 16.4.1 release, the event trace
functionality is supported for BGP. Event Trace provides the
functionality to capture BGP traces by enabling the event trace
using commands. You can disable the command if you do not
want to log traces. When convergence happens and connection
states are getting changed, the BGP traces are logged into
Event Trace infrastructure.
