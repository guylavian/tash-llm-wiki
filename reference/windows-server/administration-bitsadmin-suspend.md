---
title: "bitsadmin suspend"
type: reference
domain: windows-server
slug: administration-bitsadmin-suspend
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-suspend
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin suspend command, which suspends the specified job."
---

# bitsadmin suspend

# bitsadmin suspend



Suspends the specified job. If you suspended your job by mistake, you can use the [bitsadmin resume](bitsadmin-resume.md) switch to restart the job.

## Syntax

```
bitsadmin /suspend <job>
```

### Parameters

| Parameter | Description |
| --------- | ---------- |
| job | The job's display name or GUID. |

## Example

To suspend the job named *myDownloadJob*:


```
bitsadmin /suspend myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin resume command](bitsadmin-resume.md)

- [bitsadmin command](bitsadmin.md)
