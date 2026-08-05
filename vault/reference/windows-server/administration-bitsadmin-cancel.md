---
title: "bitsadmin cancel"
type: reference
domain: windows-server
slug: administration-bitsadmin-cancel
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-cancel
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin cancel command, which removes the job from the transfer queue and deletes all temporary files associated with the job."
---

# bitsadmin cancel

# bitsadmin cancel

Removes the job from the transfer queue and deletes all temporary files associated with the job.

## Syntax

```
bitsadmin /cancel <job>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |

## Examples

To remove the *myDownloadJob* job from the transfer queue:

```
bitsadmin /cancel myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
