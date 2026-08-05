---
title: "bitsadmin getcompletiontime"
type: reference
domain: windows-server
slug: administration-bitsadmin-getcompletiontime
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getcompletiontime
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getcompletiontime command, which retrieves the time that the job finished transferring data."
---

# bitsadmin getcompletiontime

# bitsadmin getcompletiontime

Retrieves the time that the job finished transferring data.

## Syntax

```
bitsadmin /getcompletiontime <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the time that the job named *myDownloadJob* finished transferring data:

```
bitsadmin /getcompletiontime myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
