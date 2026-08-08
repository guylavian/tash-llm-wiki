---
title: "bitsadmin setminretrydelay"
type: reference
domain: windows-server
slug: administration-bitsadmin-setminretrydelay
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-setminretrydelay
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin setminretrydelay command, which sets the minimum length of time, in seconds, that BITS waits after encountering a transient error before trying to transfer the file."
---

# bitsadmin setminretrydelay

# bitsadmin setminretrydelay

Sets the minimum length of time, in seconds, that BITS waits after encountering a transient error before trying to transfer the file.

## Syntax

```
bitsadmin /setminretrydelay <job> <retrydelay>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| retrydelay | Minimum length of time for BITS to wait after an error during transfer, in seconds. |

## Examples

To set the minimum retry delay to 35 seconds for the job named *myDownloadJob*:

```
bitsadmin /setminretrydelay myDownloadJob 35
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
