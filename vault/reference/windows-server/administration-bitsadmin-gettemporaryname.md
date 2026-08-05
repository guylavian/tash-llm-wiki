---
title: "bitsadmin gettemporaryname"
type: reference
domain: windows-server
slug: administration-bitsadmin-gettemporaryname
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-gettemporaryname
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin gettemporaryname command, which reports the temporary filename of the given file within the job."
---

# bitsadmin gettemporaryname

# bitsadmin gettemporaryname

Reports the temporary filename of the given file within the job.

## Syntax

```
bitsadmin /gettemporaryname <job> <file_index>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |
| file_index | Starts from 0. |

## Examples

To report the temporary filename of file 2 for the job named *myDownloadJob*:

```
bitsadmin /gettemporaryname myDownloadJob 1
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
