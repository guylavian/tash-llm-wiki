---
title: "bitsadmin getcustomheaders"
type: reference
domain: windows-server
slug: administration-bitsadmin-getcustomheaders
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getcustomheaders
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getcustomheaders command, which retrieves the custom HTTP headers from the job."
---

# bitsadmin getcustomheaders

# bitsadmin getcustomheaders

Retrieves the custom HTTP headers from the job.

## Syntax

```
bitsadmin /getcustomheaders <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To get the custom headers for the job named *myDownloadJob*:

```
bitsadmin /getcustomheaders myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
