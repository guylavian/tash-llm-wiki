---
title: "bitsadmin getnotifyflags"
type: reference
domain: windows-server
slug: administration-bitsadmin-getnotifyflags
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getnotifyflags
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getnotifyflags command, which retrieves the notification flags for the specified job."
---

# bitsadmin getnotifyflags

# bitsadmin getnotifyflags

Retrieves the notification flags for the specified job.

## Syntax

```
bitsadmin /getnotifyflags <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Remarks

The job can contain one or more of the following notification flags:

| Flag | Description |
| ----- | ----- |
| 0x001 | Generate an event when all files in the job have been transferred. |
| 0x002 | Generate an event when an error occurs. |
| 0x004 | Disable notifications. |
| 0x008 | Generate an event when the job is modified or transfer progress is made. |

## Examples

To retrieve the notify flags for the job named *myDownloadJob*:

```
bitsadmin /getnotifyflags myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
