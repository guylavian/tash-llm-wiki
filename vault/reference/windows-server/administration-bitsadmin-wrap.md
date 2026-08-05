---
title: "bitsadmin wrap"
type: reference
domain: windows-server
slug: administration-bitsadmin-wrap
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-wrap
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin wrap command, which wraps any line of output text extending beyond the rightmost edge of the command window to the next line."
---

# bitsadmin wrap

# bitsadmin wrap



Wraps any line of output text extending beyond the rightmost edge of the command window to the next line. You must specify this switch before any other switches.

By default, all switches except the [bitsadmin monitor](bitsadmin-monitor.md) switch, wrap the output text.

## Syntax

```
bitsadmin /wrap <job>
```

### Parameters

| Parameter | Description |
| --------- | ---------- |
| job | The job's display name or GUID. |

## Examples

To retrieve information for the job named *myDownloadJob* and wrap the output text:

```
bitsadmin /wrap /info myDownloadJob /verbose
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
