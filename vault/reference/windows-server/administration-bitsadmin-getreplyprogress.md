---
title: "bitsadmin getreplyprogress"
type: reference
domain: windows-server
slug: administration-bitsadmin-getreplyprogress
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getreplyprogress
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getreplyprogress command, which retrieves the size and progress of the server upload-reply."
---

# bitsadmin getreplyprogress

# bitsadmin getreplyprogress

Retrieves the size and progress of the server upload-reply.

> [!NOTE]
> This command isn't supported by BITS 1.2 and earlier.

## Syntax

```
bitsadmin /getreplyprogress <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the upload-reply progress for the job named *myDownloadJob*:

```
bitsadmin /getreplyprogress myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
