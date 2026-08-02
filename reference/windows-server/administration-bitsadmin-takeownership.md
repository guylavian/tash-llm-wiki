---
title: "bitsadmin takeownership"
type: reference
domain: windows-server
slug: administration-bitsadmin-takeownership
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-takeownership
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin takeownership command, which lets a user with administrative privileges take ownership of the specified job."
---

# bitsadmin takeownership

# bitsadmin takeownership

Lets a user with administrative privileges take ownership of the specified job.

## Syntax

```
bitsadmin /takeownership <job>
```

### Parameters

| Parameter | Description |
| --------- | ---------- |
| job | The job's display name or GUID. |

## Examples

To take ownership of the job named *myDownloadJob*:

```
bitsadmin /takeownership myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
