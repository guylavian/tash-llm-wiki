---
title: "bitsadmin setpriority"
type: reference
domain: windows-server
slug: administration-bitsadmin-setpriority
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-setpriority
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin setpriority command, which sets the priority of the specified job."
---

# bitsadmin setpriority

# bitsadmin setpriority

Sets the priority of the specified job.

## Syntax

```
bitsadmin /setpriority <job> <priority>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| priority | Sets the priority of the job, including:<ul><li>FOREGROUND</li><li>HIGH</li><li>NORMAL</li><li>LOW</li></ul> |

## Examples

To set the priority for the job named *myDownloadJob* to normal:

```
bitsadmin /setpriority myDownloadJob NORMAL
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
