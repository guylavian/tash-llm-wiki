---
title: "manage-bde changepin"
type: reference
domain: windows-server
slug: administration-manage-bde-changepin
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-changepin
family: administration
documentKind: "reference"
abstract: "Reference article for the manage-bde changepin command, which modifies the PIN for an operating system drive."
---

# manage-bde changepin

# manage-bde changepin

Modifies the PIN for an operating system drive. The user is prompted to enter a new PIN.

## Syntax

```
manage-bde -changepin [<drive>] [-computername <name>] [{-?|/?}] [{-help|-h}]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<drive>` | Represents a drive letter followed by a colon. |
| -computername | Specifies that manage-bde.exe will be used to modify BitLocker protection on a different computer. You can also use **-cn** as an abbreviated version of this command. |
| `<name>` | Represents the name of the computer on which to modify BitLocker protection. Accepted values include the computer's NetBIOS name and the computer's IP address. |
| -? or /? | Displays brief Help at the command prompt. |
| -help or -h | Displays complete Help at the command prompt. |

### Examples

To change the PIN used with BitLocker on drive C, type:

```
manage-bde -changepin C:
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [manage-bde command](manage-bde.md)
