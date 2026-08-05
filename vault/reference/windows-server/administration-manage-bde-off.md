---
title: "manage-bde off"
type: reference
domain: windows-server
slug: administration-manage-bde-off
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-off
family: administration
documentKind: "reference"
abstract: "Reference article for the manage-bde off command, which decrypts the drive and turns off BitLocker."
---

# manage-bde off

# manage-bde off

Decrypts the drive and turns off BitLocker. All key protectors are removed when decryption is complete.

## Syntax

```
manage-bde -off [<volume>] [-computername <name>] [{-?|/?}] [{-help|-h}]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<volume>` | Specifies a drive letter followed by a colon, a volume GUID path, or a mounted volume. |
| -computername | Specifies that manage-bde.exe will be used to modify BitLocker protection on a different computer. You can also use **-cn** as an abbreviated version of this command. |
| `<name>` | Represents the name of the computer on which to modify BitLocker protection. Accepted values include the computer's NetBIOS name and the computer's IP address. |
| -? or /? | Displays brief Help at the command prompt. |
| -help or -h | Displays complete Help at the command prompt. |

### Examples

To turn off BitLocker on drive C, type:

```
manage-bde -off C:
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [manage-bde on command](manage-bde-on.md)

- [manage-bde pause command](manage-bde-pause.md)

- [manage-bde resume command](manage-bde-resume.md)

- [manage-bde command](manage-bde.md)
