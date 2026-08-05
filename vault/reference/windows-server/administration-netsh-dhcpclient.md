---
title: "netsh dhcpclient"
type: reference
domain: windows-server
slug: administration-netsh-dhcpclient
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh-dhcpclient
family: administration
documentKind: "reference"
abstract: "Reference article for the netsh dhcpclient command, which configures and manages the DHCP client settings."
---

# netsh dhcpclient

# netsh dhcpclient

The `netsh dhcpclient` command is used to configure and manage settings for the DHCP client, including enabling tracing and exporting diagnostic logs.

## Syntax

```
netsh dhcpclient [list | help | ? | trace]
netsh dhcpclient list
netsh dhcpclient trace <enable> <disable>
netsh dhcpclient trace <dump>
```

## Parameters

| Command | Description |
|--|--|
| list | Lists the available commands in the `netsh dhcpclient` context. |
| trace `<enable>` \| `<disable>` <br><br> `<dump>` | Controls tracing for the DHCP client, allowing you to enable or disable it. This feature is helpful for troubleshooting as it generates detailed logs of DHCP client activities. You can retrieve the last 100 traces to review recent DHCP interactions. <br><br> `enable` - Enables tracing for the DHCP client. <br> `disable` - Disables tracing for the DHCP client. <br> `dump` - Exports the last 100 traces. |
| help or ? | Provides help for the list of commands available in the `netsh dhcpclient` context. |

## Example

To enable tracing for the DHCP client, run the following command:

```cmd
netsh dhcpclient trace enable
```

To dump the last 100 traces for review in a specified path, run the following command:

```cmd
netsh dhcpclient trace dump > C:\NetshTrace\dhcp_trace.txt
```
