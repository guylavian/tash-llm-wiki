---
title: "bitsadmin nowrap"
type: reference
domain: windows-server
slug: administration-bitsadmin-nowrap
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-nowrap
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin nowrap command, which truncates any line of output text extending beyond the rightmost edge of the command window."
---

# bitsadmin nowrap

# bitsadmin nowrap

Truncates any line of output text extending beyond the right-most edge of the command window. By default, all switches, except the **monitor** switch, wrap the output. Specify the **nowrap** switch before other switches.

## Syntax

```
bitsadmin /nowrap
```

## Examples

To retrieve the state for the job named *myDownloadJob* while not wrapping the output:

```
bitsadmin /nowrap /getstate myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
