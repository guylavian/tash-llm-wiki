---
title: "help"
type: reference
domain: windows-server
slug: administration-help
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/help
family: administration
documentKind: "reference"
abstract: "Reference article for the help command, which displays a list of the available commands or detailed help information on a specified command."
---

# help

# help



Displays a list of the available commands or detailed help information on a specified command. If used without parameters, **help** lists and briefly describes every system command.

## Syntax

```
help [<command>]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<command>` | Specifies the command for which to display detailed help information. |

### Examples

To view information about the **robocopy** command, type:

```
help robocopy
```

To display a list of all commands available in DiskPart, type:

```
help
```

To display detailed help information about how to use the **create partition primary** command in DiskPart, type:

```
help create partition primary
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
