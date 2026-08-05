---
title: "bitsadmin monitor"
type: reference
domain: windows-server
slug: administration-bitsadmin-monitor
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-monitor
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin monitor command, which monitors jobs in the transfer queue that are owned by the current user."
---

# bitsadmin monitor

# bitsadmin monitor

Monitors jobs in the transfer queue that are owned by the current user.

## Syntax

```
bitsadmin /monitor [/allusers] [/refresh <seconds>]
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| /allusers | Optional. Monitors jobs for all users. You must have administrator privileges to use this parameter. |
| /refresh | Optional. Refreshes the data at an interval specified by `<seconds>`. The default refresh interval is five seconds. To stop the refresh, press CTRL+C. |

## Examples

To monitor the transfer queue for jobs owned by the current user and refreshes the information every 60 seconds.

```
bitsadmin /monitor /refresh 60
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
