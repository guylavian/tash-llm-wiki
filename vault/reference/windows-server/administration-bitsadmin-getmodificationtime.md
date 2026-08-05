---
title: "bitsadmin getmodificationtime"
type: reference
domain: windows-server
slug: administration-bitsadmin-getmodificationtime
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getmodificationtime
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getmodificationtime command, which retrieves the last time the job was modified or data was successfully transferred."
---

# bitsadmin getmodificationtime

# bitsadmin getmodificationtime

Retrieves the last time the job was modified or data was successfully transferred.

## Syntax

```
bitsadmin /getmodificationtime <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the last modified time for the job named *myDownloadJob*:

```
bitsadmin /getmodificationtime myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
