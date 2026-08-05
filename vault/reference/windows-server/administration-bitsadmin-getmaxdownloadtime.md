---
title: "bitsadmin getmaxdownloadtime"
type: reference
domain: windows-server
slug: administration-bitsadmin-getmaxdownloadtime
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getmaxdownloadtime
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getmaxdownloadtime command, which retrieves the download timeout in seconds."
---

# bitsadmin getmaxdownloadtime

# bitsadmin getmaxdownloadtime



Retrieves the download timeout in seconds.

## Syntax

```
bitsadmin /getmaxdownloadtime <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To get the maximum download time for the job named *myDownloadJob* in seconds:

```
bitsadmin /getmaxdownloadtime myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
