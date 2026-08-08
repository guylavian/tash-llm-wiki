---
title: "bitsadmin setdescription"
type: reference
domain: windows-server
slug: administration-bitsadmin-setdescription
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-setdescription
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin setdescription command, which sets the description of the specified job."
---

# bitsadmin setdescription

# bitsadmin setdescription

Sets the description for the specified job.

## Syntax

```
bitsadmin /setdescription <job> <description>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| description | Text used to describe the job. |

## Examples

To retrieve the description for the job named *myDownloadJob*:

```
bitsadmin /setdescription myDownloadJob music_downloads
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
