---
title: "wbadmin get status"
type: reference
domain: windows-server
slug: administration-wbadmin-get-status
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wbadmin-get-status
family: administration
documentKind: "reference"
abstract: "Reference article for the wbadmin get status command, which reports the status of the backup or recovery operation that is currently running."
---

# wbadmin get status

# wbadmin get status

Reports the status of the backup or recovery operation that is currently running.

To get the status of the currently running backup or recovery operation using this command, you must be a member of the **Backup Operators** group or the **Administrators** group, or you must have been delegated the appropriate permissions. In addition, you must run **wbadmin** from an elevated command prompt, by right-clicking **Command Prompt**, and then selecting **Run as administrator**.

> [!IMPORTANT]
> This command doesn't stop until the backup or recovery operation is finished. The command continues to run even if you close the command window. To stop the current backup or recovery operation, run the [wbadmin stop job](wbadmin-stop-job.md) command.

## Syntax

```
wbadmin get status
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [wbadmin command](wbadmin.md)

- [wbadmin stop job command](wbadmin-stop-job.md)

- [Get-WBJob](/powershell/module/windowsserverbackup/get-wbjob)
