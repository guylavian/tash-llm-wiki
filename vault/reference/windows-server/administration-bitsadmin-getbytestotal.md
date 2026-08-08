---
title: "bitsadmin getbytestotal"
type: reference
domain: windows-server
slug: administration-bitsadmin-getbytestotal
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getbytestotal
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getbytestotal command, which Retrieves the size of the specified job."
---

# bitsadmin getbytestotal

# bitsadmin getbytestotal

Retrieves the size of the specified job.

## Syntax

```
bitsadmin /getbytestotal <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the size of the job named *myDownloadJob*:

```
bitsadmin /getbytestotal myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
