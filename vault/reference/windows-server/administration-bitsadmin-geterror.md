---
title: "bitsadmin geterror"
type: reference
domain: windows-server
slug: administration-bitsadmin-geterror
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-geterror
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin geterror command, which retrieves detailed error information for the specified job."
---

# bitsadmin geterror

# bitsadmin geterror

Retrieves detailed error information for the specified job.

## Syntax

```
bitsadmin /geterror <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the error information for the job named *myDownloadJob*:

```
bitsadmin /geterror myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
