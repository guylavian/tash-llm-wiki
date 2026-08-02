---
title: "bitsadmin setvalidationstate"
type: reference
domain: windows-server
slug: administration-bitsadmin-setvalidationstate
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-setvalidationstate
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin setvalidationstate command, which sets the content validation state of the given file within the job."
---

# bitsadmin setvalidationstate

# bitsadmin setvalidationstate

Sets the content validation state of the given file within the job.

## Syntax

```
bitsadmin /setvalidationstate <job> <file_index> <TRUE|FALSE>
```

### Parameters

| Parameter | Description |
| --------- | ---------- |
| Job | The job's display name or GUID. |
| file_index | Starts at 0. |
| TRUE or FALSE | **TRUE** turns on content validation for the specified file, while **FALSE** turns it off. |

## Examples

To set the content validation state of file 2 to TRUE for the job named *myDownloadJob*:

```
bitsadmin /setvalidationstate myDownloadJob 2 TRUE
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
