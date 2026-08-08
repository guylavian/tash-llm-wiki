---
title: "bitsadmin listfiles"
type: reference
domain: windows-server
slug: administration-bitsadmin-listfiles
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-listfiles
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin listfiles command, which lists the files in the specified job."
---

# bitsadmin listfiles

# bitsadmin listfiles

Lists the files in the specified job.

## Syntax

```
bitsadmin /listfiles <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the list of files for the job named *myDownloadJob*:

```
bitsadmin /listfiles myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
