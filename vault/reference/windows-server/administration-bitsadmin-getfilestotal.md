---
title: "bitsadmin getfilestotal"
type: reference
domain: windows-server
slug: administration-bitsadmin-getfilestotal
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getfilestotal
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getfilestotal command, which retrieves the number of files in the specified job."
---

# bitsadmin getfilestotal

# bitsadmin getfilestotal

Retrieves the number of files in the specified job.

## Syntax

```
bitsadmin /getfilestotal <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the number of files included in the job named *myDownloadJob*:

```
bitsadmin /getfilestotal myDownloadJob
```

## See Also

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
