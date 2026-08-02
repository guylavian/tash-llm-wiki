---
title: "bitsadmin setmaxdownloadtime"
type: reference
domain: windows-server
slug: administration-bitsadmin-setmaxdownloadtime
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-setmaxdownloadtime
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin setmaxdownloadtime command, which sets the download timeout in seconds."
---

# bitsadmin setmaxdownloadtime

# bitsadmin setmaxdownloadtime

Sets the download timeout in seconds.

## Syntax

```
bitsadmin /setmaxdownloadtime <job> <timeout>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| timeout | The length for the download timeout, in seconds. |

## Examples

To set the timeout for the job named *myDownloadJob* to 10 seconds.

```
bitsadmin /setmaxdownloadtime myDownloadJob 10
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
