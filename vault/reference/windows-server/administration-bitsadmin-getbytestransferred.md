---
title: "bitsadmin getbytestransferred"
type: reference
domain: windows-server
slug: administration-bitsadmin-getbytestransferred
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getbytestransferred
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getbytestransferred command, which retrieves the number of bytes transferred for the specified job."
---

# bitsadmin getbytestransferred

# bitsadmin getbytestransferred

Retrieves the number of bytes transferred for the specified job.

## Syntax

```
bitsadmin /getbytestransferred <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the number of bytes transferred for the job named *myDownloadJob*:

```
bitsadmin /getbytestransferred myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
