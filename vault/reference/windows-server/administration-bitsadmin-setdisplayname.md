---
title: "bitsadmin setdisplayname"
type: reference
domain: windows-server
slug: administration-bitsadmin-setdisplayname
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-setdisplayname
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin setdisplayname command, which sets the display name of the specified job."
---

# bitsadmin setdisplayname

# bitsadmin setdisplayname

Sets the display name for the specified job.

## Syntax

```
bitsadmin /setdisplayname <job> <display_name>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| display_name | Text used as the displayed name for the specific job. |

## Examples

To set the display name for the job to *myDownloadJob*:

```
bitsadmin /setdisplayname myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
