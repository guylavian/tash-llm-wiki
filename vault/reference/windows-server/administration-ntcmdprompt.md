---
title: "ntcmdprompt"
type: reference
domain: windows-server
slug: administration-ntcmdprompt
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ntcmdprompt
family: administration
documentKind: "reference"
abstract: "Reference article for the ntcmdprompt command, which runs the command interpreter **Cmd.exe**, rather than **Command.com**, after running a Terminate and Stay Resident (TSR) or after starting the command prompt from within an MS-DOS application."
---

# ntcmdprompt

# ntcmdprompt



Runs the command interpreter **Cmd.exe**, rather than **Command.com**, after running a Terminate and Stay Resident (TSR) or after starting the command prompt from within an MS-DOS application.

## Syntax

```
ntcmdprompt
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| /? | Displays help at the command prompt. |

#### Remarks

- When **Command.com** is running, some features of **Cmd.exe**, such as the **doskey** display of command history, aren't available. If you would prefer to run the **Cmd.exe** command interpreter after you've started a Terminate and Stay Resident (TSR) or started the command prompt from within an application based on MS-DOS, you can use the **ntcmdprompt** command. However, keep in mind that the TSR may not be available for use when you are running **Cmd.exe**. You can include the **ntcmdprompt** command in your **Config.nt** file or the equivalent custom startup file in an application's program information file (Pif).

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
