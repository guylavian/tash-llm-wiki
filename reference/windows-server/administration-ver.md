---
title: "ver"
type: reference
domain: windows-server
slug: administration-ver
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ver
family: administration
documentKind: "reference"
abstract: "Reference article for the ver command, which displays the operating system version number."
---

# ver

# ver

Displays the operating system version number. This command is supported in the Windows Command prompt (Cmd.exe), but not in any version of PowerShell.

## Syntax

```
ver
```

### Parameters

| Parameter | Description |
|--|--|
| /? | Displays help at the command prompt. |

## Examples

To obtain the version number of the operating system from the Command shell (cmd.exe), type:

```
ver
```

If you want to get the operating system version number through Windows PowerShell, type:

```powershell
$PSVersionTable.BuildVersion
```

If you want to get the operating system version number through PowerShell 7.x.x, type:

```powershell
$PSVersionTable.OS
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
