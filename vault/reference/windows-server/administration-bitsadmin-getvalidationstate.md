---
title: "bitsadmin getvalidationstate"
type: reference
domain: windows-server
slug: administration-bitsadmin-getvalidationstate
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getvalidationstate
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getvalidationstate command, which reports the content validation state of the given file within the job."
---

# bitsadmin getvalidationstate

# bitsadmin getvalidationstate

Reports the content validation state of the given file within the job.

## Syntax

```
bitsadmin /getvalidationstate <job> <file_index>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |
| file_index | Starts from 0. |

## Examples

To retrieve the content validation state of file 2 within the job named *myDownloadJob*:

```
bitsadmin /getvalidationstate myDownloadJob 1
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
