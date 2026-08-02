---
title: "exit"
type: reference
domain: windows-server
slug: administration-exit
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/exit
family: administration
documentKind: "reference"
abstract: "Reference article for exit, which exits the diskpart command interpreter."
---

# exit

# exit



Exits the command interpreter or the current batch script.

## Syntax

```
exit [/b] [<exitcode>]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| /b | Exits the current batch script instead of exiting Cmd.exe. If executed from outside a batch script, exits Cmd.exe. |
| `<exitcode>` | Specifies a numeric number. If **/b** is specified, the ERRORLEVEL environment variable is set to that number. If you are quitting the command interpreter, the process exit code is set to that number. |
| /? | Displays help at the command prompt. |

## Examples

To close the command interpreter, type:

```
exit
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
