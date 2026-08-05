---
title: "schtasks end"
type: reference
domain: windows-server
slug: administration-schtasks-end
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-end
family: administration
documentKind: "reference"
abstract: "Reference article for the schtasks end command, which stops only the instances of a program started by a scheduled task."
---

# schtasks end

# schtasks end

Stops only the instances of a program started by a scheduled task. To stop other processes, you must use the [TaskKill](taskkill.md) command.

## Syntax

```
schtasks /end /tn <taskname> [/s <computer> [/u [<domain>\]<user> [/p <password>]]]
```

### Parameters

| Parameter | Description |
|--|--|
| /tn `<taskname>` | Identifies the task that started the program. This parameter is required. |
| /s `<computer>` | Specifies the name or IP address of a remote computer (with or without backslashes). The default is the local computer. |
| /u `[<domain>]` | Runs this command with the permissions of the specified user account. By default, the command runs with the permissions of the current user of the local computer. The specified user account must be a member of the Administrators group on the remote computer. The **/u** and **/p** parameters are valid only when you use **/s**. |
| /p `<password>` | Specifies the password of the user account specified in the **/u** parameter. If you use the **/u** parameter without the **/p** parameter or the password argument, schtasks will prompt you for a password. The **/u** and **/p** parameters are valid only when you use **/s**. |
| /? | Displays help at the command prompt. |

## Examples

To stop the instance of Notepad.exe started by the *My Notepad* task, type:

```
schtasks /end /tn "My Notepad"
```

To stop the instance of Internet Explorer started by the *InternetOn* task on the remote computer, *Svr01*,type:

```
schtasks /end /tn InternetOn /s Svr01
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [schtasks change command](schtasks-change.md)

- [schtasks create command](schtasks-create.md)

- [schtasks delete command](schtasks-delete.md)

- [schtasks query command](schtasks-query.md)

- [schtasks run command](schtasks-run.md)
