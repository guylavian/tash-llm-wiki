---
title: "bitsadmin replaceremoteprefix"
type: reference
domain: windows-server
slug: administration-bitsadmin-replaceremoteprefix
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-replaceremoteprefix
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin replaceremoteprefix command, which changes the remote URL for all files in the job from *oldprefix* to *newprefix*, as necessary."
---

# bitsadmin replaceremoteprefix

# bitsadmin replaceremoteprefix

Changes the remote URL for all files in the job from *oldprefix* to *newprefix*, as necessary.

## Syntax

```
bitsadmin /replaceremoteprefix <job> <oldprefix> <newprefix>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |
| oldprefix | Existing URL prefix. |
| newprefix | New URL prefix. |

## Examples

To change the remote URL for all files in job named *myDownloadJob*, from *http://stageserver* to *http://prodserver*.

```
bitsadmin /replaceremoteprefix myDownloadJob http://stageserver http://prodserver
```

## Additional information

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
