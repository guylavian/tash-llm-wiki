---
title: "bitsadmin getfilestransferred"
type: reference
domain: windows-server
slug: administration-bitsadmin-getfilestransferred
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getfilestransferred
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getfilestransferred command, which retrieves the number of files transferred for the specified job."
---

# bitsadmin getfilestransferred

# bitsadmin getfilestransferred

Retrieves the number of files transferred for the specified job.

## Syntax

```
bitsadmin /getfilestransferred <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the number of files transferred in the job named *myDownloadJob*:

```
bitsadmin /getfilestransferred myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
