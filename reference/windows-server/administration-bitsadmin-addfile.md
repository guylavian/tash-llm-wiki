---
title: "bitsadmin addfile"
type: reference
domain: windows-server
slug: administration-bitsadmin-addfile
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-addfile
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin addfile command, which adds a file to the specified job."
---

# bitsadmin addfile

# bitsadmin addfile

Adds a file to the specified job.

## Syntax

```
bitsadmin /addfile <job> <remoteURL> <localname>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| remoteURL | The URL of the file on the server. |
| localname | The name of the file on the local computer. *Localname* must contain an absolute path to the file. |

## Examples

To add a file to the job:

```
bitsadmin /addfile myDownloadJob http://downloadsrv/10mb.zip c:\10mb.zip
```

Repeat this call for each file to add. If multiple jobs use *myDownloadJob* as their name, you must replace *myDownloadJob* with the job's GUID to uniquely identify the job.

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
