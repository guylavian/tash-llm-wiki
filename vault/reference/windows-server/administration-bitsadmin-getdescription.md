---
title: "bitsadmin getdescription"
type: reference
domain: windows-server
slug: administration-bitsadmin-getdescription
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getdescription
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getdescription command, which retrieves the description of the specified job."
---

# bitsadmin getdescription

# bitsadmin getdescription

Retrieves the description of the specified job.

## Syntax

```
bitsadmin /getdescription <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the description for the job named *myDownloadJob*:

```
bitsadmin /getdescription myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
