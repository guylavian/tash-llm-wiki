---
title: "bitsadmin info"
type: reference
domain: windows-server
slug: administration-bitsadmin-info
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-info
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin info command, which displays summary information about the specified job."
---

# bitsadmin info

# bitsadmin info

Displays summary information about the specified job.

## Syntax

```
bitsadmin /info <job> [/verbose]
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |
| /verbose | Optional. Provides detailed information about each job. |

## Examples

To retrieve information about the job named *myDownloadJob*:

```
bitsadmin /info myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin info](bitsadmin-info.md)
