---
title: "manage-bde setidentifier"
type: reference
domain: windows-server
slug: administration-manage-bde-setidentifier
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-setidentifier
family: administration
documentKind: "reference"
abstract: "Reference article for the manage-bde setidentifier command, which sets the drive identifier field on the drive to the value specified in the Provide the unique identifiers for your organization Group Policy setting."
---

# manage-bde setidentifier

# manage-bde setidentifier

Sets the drive identifier field on the drive to the value specified in the **Provide the unique identifiers for your organization** Group Policy setting.

## Syntax

```
manage-bde -setidentifier <drive> [-computername <name>] [{-?|/?}] [{-help|-h}]
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

To set BitLocker drive identifier field for C, type:

```
manage-bde -setidentifier C:
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [manage-bde command](manage-bde.md)

- [BitLocker Recovery Guide](/windows/security/information-protection/bitlocker/bitlocker-recovery-guide-plan)
