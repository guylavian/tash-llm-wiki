---
title: "bitsadmin util and enableanalyticchannel"
type: reference
domain: windows-server
slug: administration-bitsadmin-util-and-enableanalyticchannel
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-util-and-enableanalyticchannel
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin util and enableanalyticchannel command, which enables or disables the BITS client analytic channel."
---

# bitsadmin util and enableanalyticchannel

# bitsadmin util and enableanalyticchannel

Enables or disables the BITS client analytic channel.

## Syntax

```
bitsadmin /util /enableanalyticchannel TRUE|FALSE
```

| Parameter | Description |
| --------- | ---------- |
| TRUE or FALSE | **TRUE** turns on content validation for the specified file, while **FALSE** turns it off. |

## Examples

To turn the BITS client analytic channel on or off.

```
bitsadmin /util / enableanalyticchannel TRUE
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin util command](bitsadmin-util.md)

- [bitsadmin command](bitsadmin.md)
