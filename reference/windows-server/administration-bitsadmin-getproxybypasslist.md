---
title: "bitsadmin getproxybypasslist"
type: reference
domain: windows-server
slug: administration-bitsadmin-getproxybypasslist
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getproxybypasslist
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getproxybypasslist command that retrieves the proxy bypass list for the specified job."
---

# bitsadmin getproxybypasslist

# bitsadmin getproxybypasslist

Applies to: Applies to: Windows Server (All supported versions)

The `bitsadmin /getproxybypasslist` command retrieves the proxy bypass list for the specified job.

## Syntax

```
bitsadmin /getproxybypasslist <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

### Remarks

The bypass list contains the host names or IP addresses, or both, that aren't routed through a proxy. The list can contain `<local>` to refer to all servers on the same LAN. The list can be semicolon (;) or space-delimited.

## Examples

To retrieve the proxy bypass list for the job named *myDownloadJob*:

```
bitsadmin /getproxybypasslist myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
