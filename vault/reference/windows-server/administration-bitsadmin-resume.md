---
title: "bitsadmin resume"
type: reference
domain: windows-server
slug: administration-bitsadmin-resume
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-resume
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin resume command, which activates a new or suspended job in the transfer queue."
---

# bitsadmin resume

# bitsadmin resume

Activates a new or suspended job in the transfer queue. If you resumed your job by mistake, or simply need to suspend your job, you can use the [bitsadmin suspend](bitsadmin-suspend.md) switch to suspend the job.

## Syntax

```
bitsadmin /resume <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To resume the job named *myDownloadJob*:

```
bitsadmin /resume myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin suspend command](bitsadmin-suspend.md)

- [bitsadmin command](bitsadmin.md)
