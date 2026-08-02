---
title: "bitsadmin getdisplayname"
type: reference
domain: windows-server
slug: administration-bitsadmin-getdisplayname
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getdisplayname
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getdisplayname command, which retrieves the display name of the specified job."
---

# bitsadmin getdisplayname

# bitsadmin getdisplayname

Retrieves the display name of the specified job.

## Syntax

```
bitsadmin /getdisplayname <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the display name for the job named *myDownloadJob*:

```
bitsadmin /getdisplayname myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
