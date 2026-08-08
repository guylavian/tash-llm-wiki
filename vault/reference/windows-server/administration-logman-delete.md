---
title: "logman delete"
type: reference
domain: windows-server
slug: administration-logman-delete
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/logman-delete
family: administration
documentKind: "reference"
abstract: "Reference article for the logman delete command, which deletes an existing data collector."
---

# logman delete

# logman delete



Deletes an existing data collector.

## Syntax

```
logman delete <[-n] <name>> [options]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| -s `<computer name>` | Performs the command on the specified remote computer. |
| -config `<value>` | Specifies the settings file containing command options. |
| [-n] `<name>` | Name of the target object. |
| -ets | Sends commands to Event Trace Sessions directly without saving or scheduling. |
| -[-]u `<user [password]>` | Specifies the user to Run As. Entering a \* for the password produces a prompt for the password. The password is not displayed when you type it at the password prompt. |
| /? | Displays context-sensitive help. |

### Examples

To delete the data collector *perf_log*, type:

```
logman delete perf_log
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [logman command](logman.md)
