---
title: "bitsadmin getminretrydelay"
type: reference
domain: windows-server
slug: administration-bitsadmin-getminretrydelay
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getminretrydelay
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getminretrydelay command, which retrieves the length of time, in seconds, that the service waits after encountering a transient error before trying to transfer the file."
---

# bitsadmin getminretrydelay

# bitsadmin getminretrydelay

Retrieves the length of time, in seconds, that the service will wait after encountering a transient error before trying to transfer the file.

## Syntax

```
bitsadmin /getminretrydelay <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the minimum retry delay for the job named *myDownloadJob*:

```
bitsadmin /getminretrydelay myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
