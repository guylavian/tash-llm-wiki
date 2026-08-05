---
title: "bitsadmin complete"
type: reference
domain: windows-server
slug: administration-bitsadmin-complete
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-complete
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin complete command, which completes the job."
---

# bitsadmin complete

# bitsadmin complete

Completes the job. Use this switch after the job moves to the transferred state. Otherwise, only those files that have been successfully transferred will be available.

## Syntax

```
bitsadmin /complete <job>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |

## Example

To complete the *myDownloadJob* job, after it reaches the `TRANSFERRED` state:

```
bitsadmin /complete myDownloadJob
```

If multiple jobs use *myDownloadJob* as their name, you must use the job's GUID to uniquely identify it for completion.

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
