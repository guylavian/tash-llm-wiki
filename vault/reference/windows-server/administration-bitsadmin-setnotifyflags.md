---
title: "bitsadmin setnotifyflags"
type: reference
domain: windows-server
slug: administration-bitsadmin-setnotifyflags
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-setnotifyflags
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin setnotifyflags command, which sets the event notification flags for the specified job."
---

# bitsadmin setnotifyflags

# bitsadmin setnotifyflags

Sets the event notification flags for the specified job.

## Syntax

```
bitsadmin /setnotifyflags <job> <notifyflags>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| notifyflags | Can include one or more of the following notification flags, including:<ul><li>**1.** Generates an event when all files in the job have been transferred.</li><li>**2.** Generates an event when an error occurs.</li><li>**3.** Generates an event when all files have completed transfer or when an error occurs.</li><li>**4.** Disables notifications.</li></ul> |

## Examples

To set the notification flags to generate an event when an error occurs, for a job named *myDownloadJob*:

```
bitsadmin /setnotifyflags myDownloadJob 2
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
