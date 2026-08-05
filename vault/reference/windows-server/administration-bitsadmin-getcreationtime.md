---
title: "bitsadmin getcreationtime"
type: reference
domain: windows-server
slug: administration-bitsadmin-getcreationtime
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getcreationtime
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getcreationtime command, which retrieves the creation time for the specified job."
---

# bitsadmin getcreationtime

# bitsadmin getcreationtime

Retrieves the creation time for the specified job.

## Syntax

```
bitsadmin /getcreationtime <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the creation time for the job named *myDownloadJob*:

```
bitsadmin /getcreationtime myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
