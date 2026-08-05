---
title: "bitsadmin reset"
type: reference
domain: windows-server
slug: administration-bitsadmin-reset
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-reset
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin reset command, which cancels all jobs in the transfer queue owned by the current user."
---

# bitsadmin reset

# bitsadmin reset

Cancels all jobs in the transfer queue owned by the current user. You can't reset jobs created by Local System. Instead, you must be an administrator and use the task scheduler to schedule this command as a task using the Local System credentials.

> [!NOTE]
> If you have administrator privileges in BITSAdmin 1.5 and earlier, the /reset switch will cancel all the jobs in the queue. Additionally, the /allusers option isn't supported.

## Syntax

```
bitsadmin /reset [/allusers]
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| /allusers | Optional. Cancels all jobs in the queue owned by the current user. You must have administrator privileges to use this parameter. |

## Examples

To cancel all the jobs in the transfer queue for the current user.

```
bitsadmin /reset
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
