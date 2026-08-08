---
title: "bitsadmin getreplydata"
type: reference
domain: windows-server
slug: administration-bitsadmin-getreplydata
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getreplydata
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getreplydata command, which retrieves the server's upload-reply data in hexadecimal format for the job."
---

# bitsadmin getreplydata

# bitsadmin getreplydata

Retrieves the server's upload-reply data in hexadecimal format for the job.

> [!NOTE]
> This command isn't supported by BITS 1.2 and earlier.

## Syntax

```
bitsadmin /getreplydata <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the upload-reply data for the job named *myDownloadJob*:

```
bitsadmin /getreplydata myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
