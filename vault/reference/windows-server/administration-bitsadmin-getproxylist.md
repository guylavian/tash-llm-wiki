---
title: "bitsadmin getproxylist - Retrieves the proxy list for the specified job."
type: reference
domain: windows-server
slug: administration-bitsadmin-getproxylist
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getproxylist
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getproxylist command, which retrieves the proxy list for the specified job."
---

# bitsadmin getproxylist - Retrieves the proxy list for the specified job.

# bitsadmin getproxylist

Retrieves the comma-delimited list of proxy servers to use for the specified job.

## Syntax

```
bitsadmin /getproxylist <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the proxy list for the job named *myDownloadJob*:

```
bitsadmin /getproxylist myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
