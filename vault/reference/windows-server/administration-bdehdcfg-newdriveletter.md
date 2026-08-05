---
title: "bdehdcfg newdriveletter"
type: reference
domain: windows-server
slug: administration-bdehdcfg-newdriveletter
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bdehdcfg-newdriveletter
family: administration
documentKind: "reference"
abstract: "Reference article for the bdehdcfg newdriveletter command, which assigns a new drive letter to the portion of a drive used as the system drive."
---

# bdehdcfg newdriveletter

# bdehdcfg: newdriveletter

Assigns a new drive letter to the portion of a drive used as the system drive. As a best practice, we recommend not assigning a drive letter to your system drive.

## Syntax

```
bdehdcfg -target {default|unallocated|<drive_letter> shrink|<drive_letter> merge} -newdriveletter <drive_letter>
```

#### Parameters

| Parameter | Description |
| ---------| ----------- |
| `<drive_letter>` | Defines the drive letter that will be assigned to the specified target drive. |

## Examples

To assign the default drive the drive letter `P`:

```
bdehdcfg -target default -newdriveletter P:
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bdehdcfg](bdehdcfg.md)
