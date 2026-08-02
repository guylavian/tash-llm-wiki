---
title: "bitsadmin getreplyfilename"
type: reference
domain: windows-server
slug: administration-bitsadmin-getreplyfilename
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getreplyfilename
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getreplyfilename command, which gets the path of the file that contains the server upload-reply for the job."
---

# bitsadmin getreplyfilename

# bitsadmin getreplyfilename

Gets the path of the file that contains the server upload-reply for the job.

> [!NOTE]
> This command isn't supported by BITS 1.2 and earlier.

## Syntax

```
bitsadmin /getreplyfilename <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the upload-reply filename for the job named *myDownloadJob*:

```
bitsadmin /getreplyfilename myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
