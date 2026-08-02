---
title: "bitsadmin getnotifycmdline"
type: reference
domain: windows-server
slug: administration-bitsadmin-getnotifycmdline
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getnotifycmdline
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getnotifycmdline command, which retrieves the command-line command that is run when the job finishes transferring data."
---

# bitsadmin getnotifycmdline

# bitsadmin getnotifycmdline

Retrieves the command-line command to run after the specified job finishes transferring data.

> [!NOTE]
> This command isn't supported by BITS 1.2 and earlier.

## Syntax

```
bitsadmin /getnotifycmdline <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the command-line command used by the service when the job named *myDownloadJob* completes.

```
bitsadmin /getnotifycmdline myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
