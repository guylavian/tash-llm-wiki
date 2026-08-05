---
title: "wbadmin stop job"
type: reference
domain: windows-server
slug: administration-wbadmin-stop-job
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wbadmin-stop-job
family: administration
documentKind: "reference"
abstract: "Reference article for the wbadmin stop job command, which cancels the backup or recovery operation that is currently running."
---

# wbadmin stop job

# wbadmin stop job

Cancels the backup or recovery operation that is currently running.

> [!IMPORTANT]
> Canceled operations can't be restarted. You must run a canceled backup or a recovery operation from the beginning again.

To stop a backup or recovery operation using this command, you must be a member of the **Backup Operators** group or the **Administrators** group, or you must have been delegated the appropriate permissions. In addition, you must run **wbadmin** from an elevated command prompt, by right-clicking **Command Prompt**, and then selecting **Run as administrator**.

## Syntax

```
wbadmin stop job [-quiet]
```

### Parameters

| Parameter | Description |
|--|--|
| -quiet | Runs the command without prompts to the user. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [wbadmin command](wbadmin.md)
