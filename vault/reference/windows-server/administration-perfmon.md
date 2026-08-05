---
title: "perfmon"
type: reference
domain: windows-server
slug: administration-perfmon
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/perfmon
family: administration
documentKind: "reference"
abstract: "Reference article for the perfmon command, which starts the Windows Reliability and Performance Monitor in a specific standalone mode."
---

# perfmon

# perfmon

Start Windows Reliability and Performance Monitor in a specific standalone mode.

## Syntax

```
perfmon </res|report|rel|sys>
```

### Parameters

| Parameter | Description |
|--|--|
| /res | Starts the Resource View. |
| /report | Starts the System Diagnostics Data Collector Set and displays a report of the results. |
| /rel | Starts the Reliability Monitor. |
| /sys | Starts the Performance Monitor. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [Windows Performance Monitor](/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc749154(v%3dws.11))
