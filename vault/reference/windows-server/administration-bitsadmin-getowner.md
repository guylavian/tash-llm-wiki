---
title: "bitsadmin getowner"
type: reference
domain: windows-server
slug: administration-bitsadmin-getowner
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getowner
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getowner command, which retrieves the owner of the specified job."
---

# bitsadmin getowner

# bitsadmin getowner

Displays the display name or GUID of the owner of the specified job.

## Syntax

```
bitsadmin /getowner <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To display the owner for the job named *myDownloadJob*:

```
bitsadmin /getowner myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
