---
title: "Netdom movent4bdc"
type: reference
domain: windows-server
slug: administration-netdom-movent4bdc
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netdom-movent4bdc
family: administration
documentKind: "reference"
abstract: "Netdom movent4bdc is a command-line utility that renames a Windows NT 4.0 backup domain controller in Windows Server."
---

# Netdom movent4bdc

# netdom movent4bdc

The `netdom movent4bdc` command renames a Windows NT 4.0 backup domain controller (DC). It's available if you have the Active Directory Domain Services (AD DS) server role installed. It's also available if you install the AD DS tools that are part of the Remote Server Administration Tools (RSAT). To use `netdom movent4bdc`, you must run the command from an elevated command prompt.

This command is specific to legacy Windows Server operating systems.

## Syntax

```
netdom movent4bdc machine [/Domain:domain] [/Reboot[:Time in seconds]]
```

## Parameters

| Parameter | Description |
|---|---|
| `<machine>` | Specifies the name of the backup DC that you want to rename. |
| `/domain:<Domain>` | Specifies the new name of the domain. |
| `/reboot:<seconds>` | Shuts down the computer and automatically reboots after the move operation completes. The *seconds* value is the number of seconds before automatic shutdown. The default is **20** seconds. |
| `help` \| `/?` | Displays help at the command prompt. |

## Examples

To rename **OldBDC** to **NewBDC** for the domain **reskita**, run the following command:

```cmd
netdom movent4bdc oldbdc newbdc /domain:reskita
```

## See also

[Command-Line Syntax Key](command-line-syntax-key.md)
